import random
import time
# a

def lire_temperature():
    
    return round(random.uniform(15, 40), 1)


def lire_humidite():
    
    return round(random.uniform(20, 80), 1)


def analyser_conditions(temp, humid):
    alertes = []
    if temp > 30:
        alertes.append("⚠️ Alerte : Il fait trop chaud !")
    elif temp < 18:
        alertes.append("⚠️ Alerte : Il fait trop froid !")

    if humid < 30:
        alertes.append("⚠️ Alerte : Humidité trop basse !")
    elif humid > 70:
        alertes.append("⚠️ Alerte : Humidité trop élevée !")

    return alertes


def simulateur(nb_mesures=10, pause=1):
    print("Début de la simulation météo...\n")

    for i in range(nb_mesures):
        temp = lire_temperature()
        humid = lire_humidite()
        print(f"Mesure {i+1} - Température: {temp}°C, Humidité: {humid}%")

        alertes = analyser_conditions(temp, humid)
        if alertes:
            for alerte in alertes:
                print(alerte)
        else:
            print("Conditions normales.")

        print("-" * 40)
        time.sleep(pause)  

    print("\nFin de la simulation.")


simulateur()