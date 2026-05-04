from weather import get_weather
from ai_analysis import analyser_meteo

def afficher_meteo(ville):
    print(f"\n Recherche météo pour : {ville}")
    print("-" * 40)
    
    meteo = get_weather(ville)
    
    if meteo:
        print(f"Ville       : {meteo['ville']}, {meteo['pays']}")
        print(f"Température : {meteo['temperature']}°C")
        print(f"Ressenti    : {meteo['ressenti']}°C")
        print(f"Humidité    : {meteo['humidite']}%")
        print(f"Ciel        : {meteo['description']}")
        print(f"Vent        : {meteo['vent']} m/s")
        
        print("\n Analyse IA :")
        print("-" * 40)
        analyse = analyser_meteo(meteo)
        print(analyse)
    else:
        print("Ville introuvable. Vérifie le nom.")

if __name__ == "__main__":
    ville = input("Entre le nom d'une ville : ")
    afficher_meteo(ville)