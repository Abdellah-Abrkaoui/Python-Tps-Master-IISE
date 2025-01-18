# get file
def get_file():
    while True:
        try:
            file_name = input("saisir le nom du fichier : ")
            with open(file_name, "r") as file:
                print(f"fichier '{file_name}' est ouvert avec succes")
                return file_name
        except FileNotFoundError:
            print(f"Erreur : Le fichier '{file_name}' n'existe pas")
        except Exception as e:
            print(f"Une erreur inattendue : {e}")

# get positive integer
def get_positive_integer():

    while True:
        try:
            value_input = input("saisir un entier strictement positif : ")
            value = int(value_input)
            if value > 0:
                return value
            else:
                print("Erreur : L'entier doit etre strictement positif")
        except ValueError:
            print("Erreur : La saisie doit etre un entier valide.")
        except Exception as e:
            print(f"Une erreur inattendue : {e}")

# Appel des fonctions
file_name = get_file()
positive_integer = get_positive_integer()
print(f"\n- Fichier selectionne : {file_name}\n- Entier positif saisi : {positive_integer}")
