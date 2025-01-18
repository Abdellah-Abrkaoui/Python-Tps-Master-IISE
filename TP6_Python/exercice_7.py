# Journalisations des exceptions


import logging
file = "TP6_Python/error.log"

def log_error(message):
    logging.basicConfig(filename=file, level=logging.ERROR)
    logging.error(message)


# Lecture de ficiher


def read_file(filename):
    fichier = None
    try:
        fichier = open(filename, "r") 
        content = fichier.read()
        return content
    except FileNotFoundError :
        error_msg = f"Erreur : Le fichier '{filename}' n'existe pas."
        log_error(error_msg)
    finally :
        if fichier:
            fichier.close()
            print("fin de programme")



fille  = "exemple.txt"
content = read_file(fille)

if content:
    print(content)
else:
    print(f"Impossible de lire le fichier '{fille}'.")