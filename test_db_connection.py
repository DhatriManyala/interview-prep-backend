import psycopg2
import os

# If you use a .env file, uncomment these two lines:
from dotenv import load_dotenv
load_dotenv()

DB_HOST = os.getenv("DB_HOST", "interviewprepdb.cvwm8kk268pf.eu-north-1.rds.amazonaws.com")
DB_PORT = os.getenv("DB_PORT", "5432")
DB_NAME = os.getenv("DB_NAME", "interviewprepdb")
DB_USER = os.getenv("DB_USER", "admin1")
DB_PASS = os.getenv("DB_PASS", "interviewprepdb1")

try:
    conn = psycopg2.connect(
        host=DB_HOST,
        port=DB_PORT,
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASS,
        connect_timeout=5
    )
    print("Connection to database successful!")
    conn.close()
except Exception as e:
    print("Failed to connect to database.")
    print(e)