# **Ethiopian Medical Data Warehouse**

## **Project Overview**

This project is a **data warehouse** built to store, clean, transform, and analyze **Ethiopian medical business data** scraped from Telegram channels. The data pipeline includes:
✅ **Web Scraping** (Telegram API & Telethon)\
✅ **Data Cleaning & Transformation** (Pandas & DBT)\
✅ **Object Detection** (YOLOv5 for image processing)\
✅ **Database Storage** (PostgreSQL for structured data)\
✅ **API Development** (FastAPI for data access)

---

## **Tech Stack**

- **Programming Language**: Python 🐍
- **Data Scraping**: Telethon, BeautifulSoup, Scrapy
- **Data Processing**: Pandas, NumPy, DBT (Data Build Tool)
- **Database**: PostgreSQL
- **Object Detection**: YOLOv5, OpenCV, Torch
- **API Development**: FastAPI, Uvicorn

---

## **Project Structure**

```
ethiopian-medical-data-warehouse/
│── data_scraping/
│   ├── scraper.py           # Telegram data scraper
│── data_cleaning/
│   ├── data_cleaning.py      # Cleans and transforms scraped data
│── dbt_models/
│   ├── transformations/
│   │   ├── cleaned_messages.sql # DBT model for data transformation
│── object_detection/
│   ├── detector.py          # YOLOv5 object detection script
│── api/
│   ├── main.py              # FastAPI application
│── database/
│   ├── load_to_database.py  # Inserts cleaned data into PostgreSQL
│── notebooks/
│   ├── data_cleaning.ipynb  # Jupyter Notebook for exploratory data analysis
│── requirements.txt         # Project dependencies
│── README.md                # Project documentation
```

---

## **Installation & Setup**

### **1️⃣ Clone the Repository**

```bash
git clone https://github.com/your-username/ethiopian-medical-data-warehouse.git
cd ethiopian-medical-data-warehouse
```

### **2️⃣ Set Up a Virtual Environment**

```bash
python -m venv env
source env/bin/activate  # macOS/Linux
env\Scripts\activate  # Windows
```

### **3️⃣ Install Dependencies**

```bash
pip install -r requirements.txt
```

### **4️⃣ Set Up Database (PostgreSQL)**

1. Create a database:

```sql
CREATE DATABASE ethiopian_medical_db;
```

2. Create tables (example):

```sql
CREATE TABLE telegram_data (
    id SERIAL PRIMARY KEY,
    channel TEXT,
    message_id BIGINT UNIQUE,
    date TIMESTAMP,
    sender_id BIGINT,
    text TEXT,
    image_data BYTEA
);
```

### **5️⃣ Configure DBT**

```bash
dbt debug
dbt run
```

### **6️⃣ Run the API**

```bash
uvicorn api.main:app --reload
```

Then, open:\
👉 **[http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)** (Swagger UI for API testing)

---

## **Key Features**

✔ **Automated Data Pipeline** - Scrapes, cleans, and stores data automatically.\
✔ **Real-Time Image Analysis** - Uses **YOLOv5** for object detection on medical business images.\
✔ **Structured Data Storage** - PostgreSQL for scalable and efficient querying.\
✔ **REST API for Data Access** - FastAPI serves data through API endpoints.

---

## **Endpoints (FastAPI)**

| Method | Endpoint              | Description                            |
| ------ | --------------------- | -------------------------------------- |
| `GET`  | `/messages/`          | Fetch all cleaned messages             |
| `GET`  | `/messages/{channel}` | Fetch messages from a specific channel |
| `GET`  | `/detections/`        | Fetch object detection results         |
| `POST` | `/scrape/`            | Trigger Telegram scraping manually     |

---

## **Next Steps**

🚀 Deploy the API to a cloud service (AWS, Azure, etc.)\
📊 Perform additional analysis using NLP for sentiment analysis\
📦 Expand YOLO training for better object recognition in medical images

---

### **Contributors**

👨‍💻 **kaleab Bekele**- Data Engineer\
📅 **Completion Date** - February 2025

🔥 **Happy Coding!** 🚀

