# Renommer et Supprimer des Fichiers


# rename a file using os.rename()

import os

source = "TP5_Python/files/phrase.txt"
destination = "TP5_Python/files/anciennes_phrases.txt"

try :
    os.rename(source,destination)
    print(f"file {source} renamed successfully to {destination}")
except OSError as error:
    print(error)


# remove file

try :
    os.remove(destination)
    print(f"file {destination} removed succesfully")
except FileNotFoundError :
    print("file not found")
except OSError as error:
    print(error)

