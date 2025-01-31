import os
import psycopg2
import pandas as pd
from dotenv import load_dotenv

load_dotenv()

# Database connection configuration
DB_CONFIG = {
    'dbname': os.getenv('DB_NAME'),
    'user': os.getenv('DB_USER'),
    'password': os.getenv('DB_PASSWORD'),
    'host': 'localhost',
    'port': 5432
}

# Paths
CLEANED_CSV = "../data/scraped_data/cleaned_data.csv"
IMAGE_DIR = "../data/scraped_images"

# Connect to PostgreSQL
def connect_to_db():
    try:
        conn = psycopg2.connect(**DB_CONFIG)
        print("Database connection successful.")
        return conn
    except Exception as e:
        print(f"Error connecting to database: {e}")
        return None

# Function to read image from the filesystem and return as binary
def get_image_data(image_filename):
    """Reads image from the filesystem and returns it as binary data."""
    image_path = os.path.join(IMAGE_DIR, image_filename)
    try:
        with open(image_path, "rb") as img_file:
            return img_file.read()  # Returns binary data of the image
    except FileNotFoundError:
        print(f"Image file {image_filename} not found.")
        return None

# Insert data into PostgreSQL
def load_csv_to_db(conn):
    try:
        df = pd.read_csv(CLEANED_CSV)
        cursor = conn.cursor()
        for _, row in df.iterrows():
            # Validate and get image data as binary
            image_file = row.get('image', None)
            image_data = get_image_data(image_file) if pd.notna(image_file) else None

            # Insert data into the database
            cursor.execute("""
                INSERT INTO telegram_data (channel, message_id, date, sender_id, text, image_data)
                VALUES (%s, %s, %s, %s, %s, %s)
            """, (
                row['channel'],
                row['message_id'],
                row['date'],
                row['sender_id'],
                row['text'],
                image_data  # Insert the binary data for image
            ))
        conn.commit()
        print(f"Successfully loaded data into the database.")
    except Exception as e:
        print(f"Error loading data into the database: {e}")

# Main function
if __name__ == "__main__":
    conn = connect_to_db()
    if conn:
        load_csv_to_db(conn)
        conn.close()
