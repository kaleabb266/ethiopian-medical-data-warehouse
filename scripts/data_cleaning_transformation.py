import os
import json
import pandas as pd

# Define Paths
DATA_DIR = os.path.abspath("scraped_data")
CONSOLIDATED_JSON = os.path.join(DATA_DIR, "all_channels_data.json")
CLEANED_CSV = os.path.join(DATA_DIR, "cleaned_data.csv")

# Ensure the data directory exists
os.makedirs(DATA_DIR, exist_ok=True)

# Step 1: Convert JSON to CSV
def json_to_csv(json_file, csv_file):
    """Converts a JSON file to CSV format."""
    if not os.path.exists(json_file):
        print(f"Error: JSON file '{json_file}' not found.")
        return
    try:
        with open(json_file, "r", encoding="utf-8") as f:
            data = json.load(f)  # Correctly load JSON list
        df = pd.DataFrame(data)
        df.to_csv(csv_file, index=False)
        print(f"Converted JSON to CSV: {csv_file}")
    except Exception as e:
        print(f"Error converting JSON to CSV: {e}")

# Step 2: Remove Duplicates Based on Message ID
def remove_duplicates(csv_file):
    """Removes duplicate rows based on message_id."""
    if not os.path.exists(csv_file):
        print(f"Error: CSV file '{csv_file}' not found.")
        return
    try:
        df = pd.read_csv(csv_file)
        initial_count = len(df)
        df = df.drop_duplicates(subset=["message_id"], keep="first")  # Keep first occurrence
        final_count = len(df)
        print(f"Removed {initial_count - final_count} duplicate rows.")
        df.to_csv(csv_file, index=False)
    except Exception as e:
        print(f"Error removing duplicates: {e}")

# Step 3: Handle Missing Values
def handle_missing_values(csv_file):
    """Handles missing values in the CSV."""
    if not os.path.exists(csv_file):
        print(f"Error: CSV file '{csv_file}' not found.")
        return
    try:
        df = pd.read_csv(csv_file)
        # Fill missing text messages
        df["text"] = df["text"].fillna("No text provided")
        # Handle missing dates: Use today's date if empty
        df["date"] = pd.to_datetime(df["date"], errors="coerce")
        df["date"].fillna(pd.Timestamp.today(), inplace=True)
        df.to_csv(csv_file, index=False)
        print("Handled missing values.")
    except Exception as e:
        print(f"Error handling missing values: {e}")

# Step 4: Standardize & Validate Data
def standardize_data_formats(csv_file):
    """Standardizes data formats."""
    if not os.path.exists(csv_file):
        print(f"Error: CSV file '{csv_file}' not found.")
        return
    try:
        df = pd.read_csv(csv_file)
        df["date"] = pd.to_datetime(df["date"]).dt.strftime("%Y-%m-%dT%H:%M:%S")
        df["text"] = df["text"].str.strip()
        df.to_csv(csv_file, index=False)
        print("Standardized data formats.")
    except Exception as e:
        print(f"Error standardizing data formats: {e}")

# Run the pipeline
if __name__ == "__main__":
    print(f"Checking or creating data directory: {DATA_DIR}")
    
    json_to_csv(CONSOLIDATED_JSON, CLEANED_CSV)
    remove_duplicates(CLEANED_CSV)
    handle_missing_values(CLEANED_CSV)
    standardize_data_formats(CLEANED_CSV)
