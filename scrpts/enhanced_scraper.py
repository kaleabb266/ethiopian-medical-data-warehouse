import logging
import os
from telethon import TelegramClient, events, errors
from datetime import datetime
import json
import asyncio
from telethon.tl.types import MessageMediaPhoto
from dotenv import load_dotenv



# Configure logging
logging.basicConfig(
    filename='telegram_scraper.log',
    filemode='a',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Configuration variables
load_dotenv()
API_ID = os.getenv("API_ID")
API_HASH = os.getenv("API_HASH")
SESSION_NAME = os.getenv("SESSION_NAME")


CHANNELS = [
    'https://t.me/DoctorsET',
    'https://t.me/CheMed123',
    'https://t.me/lobelia4cosmetics',
    'https://t.me/yetenaweg',
    'https://t.me/EAHCI'
]

# Temporary data storage directories
DATA_DIR = "scraped_data"
IMAGE_DIR = "scraped_images"
os.makedirs(DATA_DIR, exist_ok=True)
os.makedirs(IMAGE_DIR, exist_ok=True)

ALL_DATA_FILE = os.path.join(DATA_DIR, "all_channels_data.json")

def save_to_consolidated_file(data):
    """Save all scraped data to a single JSON file in structured format."""
    try:
        if os.path.exists(ALL_DATA_FILE):
            with open(ALL_DATA_FILE, "r", encoding="utf-8") as file:
                existing_data = json.load(file)
        else:
            existing_data = []

        existing_data.append(data)

        with open(ALL_DATA_FILE, "w", encoding="utf-8") as file:
            json.dump(existing_data, file, indent=4)

        logging.info("Saved data successfully")
    except Exception as e:
        logging.error(f"Failed to save data: {e}")


async def save_image(client, media, filename):
    """Download and save images from a message."""
    try:
        filepath = os.path.join(IMAGE_DIR, filename)
        await client.download_media(media, file=filepath)
        logging.info(f"Saved image to {filepath}")
    except Exception as e:
        logging.error(f"Failed to save image: {e}")

async def scrape_channel(client, channel_url):
    """Scrape text and images from a Telegram channel."""
    try:
        logging.info(f"Starting scrape for channel: {channel_url}")
        async for message in client.iter_messages(channel_url, limit=100):
            data = {
                "channel": channel_url,
                "message_id": message.id,
                "date": message.date.isoformat(),
                "sender_id": message.sender_id,
                "text": message.text or None,
            }
            if isinstance(message.media, MessageMediaPhoto):
                filename = f"{channel_url.split('/')[-1]}_{message.id}.jpg"
                await save_image(client, message.media, filename)
                data["image"] = filename

            save_to_consolidated_file(data)

        logging.info(f"Completed scrape for channel: {channel_url}")
    except errors.FloodWaitError as e:
        logging.warning(f"Flood wait error: Waiting for {e.seconds} seconds")
        await asyncio.sleep(e.seconds)
    except Exception as e:
        logging.error(f"Failed to scrape channel {channel_url}: {e}")

async def main():
    """Main function to initialize scraping."""
    async with TelegramClient(SESSION_NAME, API_ID, API_HASH) as client:
        for channel in CHANNELS:
            await scrape_channel(client, channel)

if __name__ == "__main__":
    try:
        logging.info("Starting Telegram scraping script")
        asyncio.run(main())
    except KeyboardInterrupt:
        logging.info("Scraping stopped by user.")
    except Exception as e:
        logging.critical(f"An unexpected error occurred: {e}")
