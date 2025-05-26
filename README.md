# Weather-Tracker-App
A Python app that uses the OpenWeatherMap API to track current weather and forecasts, store data in a local database, and display interactive charts using Streamlit.

A simple weather forecast application built with Python, Streamlit, and SQLite.
The app fetches current and forecast weather data from WeatherAPI, caches results in a local database, and displays weather information for any city.

Features
Get current weather for a city

Get weather forecast for up to 3 days

Cache data locally in SQLite to reduce API calls

Display weather condition with icons

Simple and clean Streamlit web interface

Requirements
Python 3.8+

Packages listed in requirements.txt

Setup
Clone the repository:

bash
git clone <url>
cd weather-tracker

Create a .env file in the project root with your WeatherAPI key:

env
API_KEY=your_weatherapi_key_here
Install dependencies:

bash
pip install -r requirements.txt
Running the App
Run the Streamlit app with:

bash
streamlit run app.py
Open the URL shown in your terminal (usually http://localhost:8501) in your browser.

Project Structure
app.py: Main Streamlit app script

api_client.py: Handles calls to WeatherAPI

database.py: SQLite database creation, insertion, and query logic

.env: Environment file containing your API key

Notes
The forecast supports up to 3 days only (due to API limits)

Data is cached locally in weather.db SQLite file

Please respect WeatherAPI's rate limits to avoid blocked requests