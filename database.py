import sqlite3
import os
import datetime

db_name = 'weather.db'

def check_database():
    db_exists = os.path.exists(db_name)
    return db_exists

def create_db():
    if not check_database():
        conn = sqlite3.connect(db_name)
        cursor = conn.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS current_weather_data (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            city TEXT NOT NULL,
            date TEXT NOT NULL,
            temperature REAL,
            sensation REAL,
            humidity INTEGER,
            condition TEXT,
            condition_icon TEXT,
            UNIQUE(city, date)
        );
        """)

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS forecast_weather_data (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            city TEXT NOT NULL,
            date TEXT NOT NULL,
            condition TEXT,
            condition_icon TEXT,
            max_temp REAL,
            min_temp REAL,
            UNIQUE(city, date)           
        );
        """)
        conn.commit()
        conn.close()

def insert_to_SQL(city, current_date, condition, condition_icon, temperature=0, sensation=0, humidity=0, days=0, max_temp=0, min_temp=0):
    create_db()

    if days == 0:
        query = f"""INSERT INTO current_weather_data (city, date, temperature, sensation, humidity, condition, condition_icon) 
        VALUES ('{city}', '{current_date}', {temperature}, {sensation}, {humidity}, '{condition}', '{condition_icon}');"""

    else:
        query = f"""INSERT INTO forecast_weather_data (city, date, condition, condition_icon, max_temp, min_temp) 
        VALUES ('{city}', '{current_date}', '{condition}', '{condition_icon}', {max_temp}, {min_temp});"""
    
    print(query)

    with sqlite3.connect(db_name) as connection:
        cursor = connection.cursor()
        try:
            cursor.execute(query)
            return True
        except Exception as e:
            print(e)
            return False

def check_if_exists(city, date, days=0):
    create_db()

    if days == 0:
        query = f"""SELECT * FROM current_weather_data where city = '{city}' AND date = '{date}'"""
    
    else:
        final_date = date + datetime.timedelta(days=days)
        # query = f"""SELECT * FROM forecast_weather_data where city = '{city}' AND date BETWEEN '{date}' AND '{final_date}' ORDER BY DATE"""
        query = f"""WITH date_count AS (
            SELECT COUNT(DISTINCT date) AS cnt
            FROM forecast_weather_data
            WHERE city = '{city}' AND date BETWEEN '{date}' AND '{final_date}'
        )
        SELECT *
        FROM forecast_weather_data
        WHERE city = '{city}' AND date BETWEEN '{date}' AND '{final_date}'
        AND (SELECT cnt FROM date_count) = ((julianday('{final_date}') - julianday('{date}')) + 1)
        ORDER BY date;"""
        print(query)

    with sqlite3.connect(db_name) as connection:
        cursor = connection.cursor()
        cursor.execute(query)
        result = cursor.fetchall()

    return result