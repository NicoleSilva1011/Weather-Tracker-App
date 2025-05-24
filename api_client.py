import requests
import os
from dotenv import load_dotenv
import json

load_dotenv(".env")

api_key = os.environ.get("API_KEY")

url = "http://api.weatherapi.com/v1/"


def get_current_weather(city):
    response = requests.get(url + f'current.json?key={api_key}&q={city}&aqi=no')
    if response.status_code == 200:
        return json.loads(response.content)
    else:
        print(f"Erro: {response.status_code}")
        return {}
    
def get_next_days_weather(city, days):
    response = requests.get(url + f'forecast.json?key={api_key}&q={city}&days={days}&aqi=no&alerts=no')
    if response.status_code == 200:
        return json.loads(response.content)
    else:
        print(f"Erro: {response.status_code}")
        return {}