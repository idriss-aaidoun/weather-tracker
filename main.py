from weather import get_weather
from ai_analysis import analyser_meteo        # Groq
from ai_local import analyser_meteo_local     # Ollama

def afficher_meteo(ville, moteur="groq"):
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

        if moteur == "local":
            print(" Modèle : Ollama (local)")
            analyse = analyser_meteo_local(meteo)
        else:
            print(" Modèle : Groq (cloud)")
            analyse = analyser_meteo(meteo)

        print(analyse)
    else:
        print("Ville introuvable. Vérifie le nom.")

def comparer_villes():
    villes = input("Entre les villes séparées par une virgule : ").split(",")
    print(f"\n{'Ville':<20} {'Temp':>8} {'Humidité':>10} {'Vent':>8}")
    print("-" * 50)
    for ville in villes:
        meteo = get_weather(ville.strip())
        if meteo:
            print(f"{meteo['ville']:<20} {meteo['temperature']:>7}°C {meteo['humidite']:>9}% {meteo['vent']:>6}m/s")
        else:
            print(f"{ville.strip():<20} introuvable")

if __name__ == "__main__":
    print("\n=== WEATHER TRACKER ===")
    print("1 — Météo d'une ville (Groq)")
    print("2 — Météo d'une ville (Ollama local)")
    print("3 — Comparer plusieurs villes")

    choix = input("\nTon choix : ")

    if choix == "1":
        ville = input("Ville : ")
        afficher_meteo(ville, moteur="groq")
    elif choix == "2":
        ville = input("Ville : ")
        afficher_meteo(ville, moteur="local")
    elif choix == "3":
        comparer_villes()
    else:
        print("Choix invalide.")