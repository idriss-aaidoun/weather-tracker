from groq import Groq
import os
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def analyser_meteo(meteo):
    prompt = f"""
    Voici les données météo actuelles pour {meteo['ville']} ({meteo['pays']}) :
    - Température : {meteo['temperature']}°C
    - Ressenti : {meteo['ressenti']}°C
    - Humidité : {meteo['humidite']}%
    - Ciel : {meteo['description']}
    - Vent : {meteo['vent']} m/s

    Donne une analyse courte et utile en 4 points :
    1. Comment est ce temps en général ?
    2. Que conseilles-tu de porter ou d'emporter ?
    3. Est-ce un bon moment pour sortir ou faire du sport dehors ?
    4. Quelles sont les précautions à prendre ?
    Réponds de façon naturelle et sympathique, en français, en 4-5 lignes max.
    """

    try:
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=500
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Erreur lors de l'analyse Groq : {e}"