import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("OPENWEATHER_API_KEY")
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def get_weather(city):
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric",  # Celsius
        "lang": "fr"
    }
    
    response = requests.get(BASE_URL, params=params)
    
    if response.status_code == 200:
        data = response.json()
        return {
            "ville": data["name"],
            "pays": data["sys"]["country"],
            "temperature": data["main"]["temp"],
            "ressenti": data["main"]["feels_like"],
            "humidite": data["main"]["humidity"],
            "description": data["weather"][0]["description"],
            "vent": data["wind"]["speed"]
        }
    else:
        return None