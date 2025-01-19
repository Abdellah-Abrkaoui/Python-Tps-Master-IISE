# Utilisation des modules standards

# 1 > Savoir le répertoire courant
import os

rep = os.getcwd()
print(rep) # C:\Users\abdellah\Desktop\Master\S7\Python\Python TPs


# 2 > Savoir La date et l'heure actuelles
from datetime import datetime

date = datetime.now()
print(date) # ex : 2025-01-19 13:49:16.059919

date_format = date.strftime("%d/%m/%Y %H:%M:%S")
print(date_format) # ex : 19/01/2025 13:49:16


# 3 > Savoir La racine carrée d'un nombre donné par l'utilisateur
from math import sqrt
try:
    user_input = float(input("Enter un nombre : "))
    if user_input < 0 :
        print("Impossible de calculer la racine carree d'un nombre negatif")
    else:
        racine_carre = sqrt(user_input)
        print(f"La racine carre de {user_input} est : {round(racine_carre,2)}")
except ValueError:
    print("Le nombre doit etre positive")

