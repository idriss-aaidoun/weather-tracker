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

    try:
        response = requests.get(BASE_URL, params=params, timeout=10)
    except requests.exceptions.RequestException as e:
        print(f"Erreur réseau lors de la récupération de la météo : {e}")
        return None

    if response.status_code == 200:
        try:
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
        except (KeyError, ValueError) as e:
            print(f"Réponse météo inattendue : {e}")
            return None
    else:
        return None