# Gestion des Exceptions dans les Boucles


def get_positive_integer():
    while True :
        try :
            user_input = int(input("Enter un nombre : "))
            if user_input > 0 :
                return user_input
            else :
                print("L'entier doit etre positif strictement")
        except ValueError:
            print("Entree invalide")


res = get_positive_integer()
print(f"{res}")

    