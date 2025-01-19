# Utilisation de bibliothèques tierces

import pandas as pd

df = pd.read_csv("files/employes.csv")
print("Les cinq premieres lignes du fichier :")
print(df.head())


# calculons l'age moyenne des employes
Age = df.columns[1]
mean_age = df["Age"].mean()
print(f"l'age moyenne des employes est : {mean_age}")

