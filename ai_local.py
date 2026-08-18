import requests
import json

OLLAMA_URL = "http://localhost:11434/api/chat"
MODEL = "llama3.2"  

def analyser_meteo_local(meteo):
    prompt = f"""
    Voici les données météo actuelles pour {meteo['ville']} ({meteo['pays']}) :
    - Température : {meteo['temperature']}°C
    - Ressenti : {meteo['ressenti']}°C
    - Humidité : {meteo['humidite']}%
    - Ciel : {meteo['description']}
    - Vent : {meteo['vent']} m/s

    Donne une analyse courte et utile en 3 points :
    1. Comment est ce temps en général ?
    2. Que conseilles-tu de porter ou d'emporter ?
    3. Est-ce un bon moment pour sortir ?

    Réponds en français, 4-5 lignes max.
    """

    payload = {
        "model": MODEL,
        "messages": [{"role": "user", "content": prompt}],
        "stream": False  # on veut la réponse complète d'un coup
    }

    try:
        response = requests.post(OLLAMA_URL, json=payload, timeout=30)
    except requests.exceptions.RequestException as e:
        return f"Erreur Ollama : impossible de contacter le serveur local ({e})"

    if response.status_code == 200:
        try:
            return response.json()["message"]["content"]
        except (KeyError, ValueError) as e:
            return f"Erreur Ollama : réponse inattendue ({e})"
    else:
        return f"Erreur Ollama : {response.status_code}"