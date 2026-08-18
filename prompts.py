def build_prompt(meteo, instructions):
    return f"""
    Voici les données météo actuelles pour {meteo['ville']} ({meteo['pays']}) :
    - Température : {meteo['temperature']}°C
    - Ressenti : {meteo['ressenti']}°C
    - Humidité : {meteo['humidite']}%
    - Ciel : {meteo['description']}
    - Vent : {meteo['vent']} m/s

    {instructions}
    """
