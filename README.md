# Weather-Tracker-App

A Python application that provides current weather and forecast information for up to 3 days using the WeatherAPI. The app features a clean and interactive web interface built with Streamlit and stores weather data locally in an SQLite database to optimize API usage.

## Features

- **Current Weather**: Fetch and display the current weather conditions for any city, including temperature, humidity, and weather description with icons.
- **Weather Forecast**: Get weather forecasts for up to 3 days, including maximum and minimum temperatures, and conditions.
- **Local Caching**: Store weather data in an SQLite database to minimize redundant API calls.
- **Interactive Interface**: Simple and user-friendly interface built with Streamlit.

## Requirements

- Python 3.8+
- Dependencies listed in `requirements.txt`

## Setup

1. **Clone the repository:**
   ```bash
   git clone <url>
   cd Weather-Tracker-App
   ```

2. **Create a `.env` file:**
   In the project root, create a `.env` file and add your WeatherAPI key:
   ```env
   API_KEY=your_weatherapi_key_here
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## Running the App

1. **Start the Streamlit app:**
   ```bash
   streamlit run app.py
   ```

2. **Open the app in your browser:**
   The app will usually be available at [http://localhost:8501](http://localhost:8501).

## Project Structure

- `app.py`: Main Streamlit app script. Handles user input and displays weather data.
- `api_client.py`: Contains functions to fetch weather data from WeatherAPI.
- `database.py`: Manages SQLite database creation, data insertion, and queries.
- `requirements.txt`: Lists all Python dependencies.
- `weather.db`: SQLite database file for caching weather data.

## How It Works

1. **User Input**: Enter a city name and optionally select the number of forecast days (0-3).
2. **API Call**: The app fetches data from WeatherAPI using the `api_client.py` module.
3. **Data Storage**: Weather data is cached in the SQLite database (`weather.db`) using `database.py`.
4. **Display**: The app displays the weather data in a clean and interactive interface.