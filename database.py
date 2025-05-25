import sqlite3
import os

db_name = 'weather.db'

def check_database():
    db_exists = os.path.exists(db_name)
    return db_exists

def create_db():
    if not check_database():
        conn = sqlite3.connect(db_name)
        cursor = conn.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS weather_data (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            city TEXT NOT NULL,
            date TEXT NOT NULL,
            temperature REAL,
            sensation REAL,
            humidity INTEGER,
            condition TEXT,
            condition_icon TEXT,
            max_temp REAL,
            min_temp REAL,
            UNIQUE(city, date)
        );
        """)
        conn.commit()
        conn.close()
