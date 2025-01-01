# Copie et Déplacement de Fichiers

# writing content in file journal.txt

file = "TP5_Python/files/journal.txt"

phrases = []
for i in range(1,4):
    ph = input(f"enter sentence {i} : > ")
    phrases.append(ph)

with open(file, "w") as myFile :
    for i in phrases:
        myFile.write(i + "\n")


# copy "journal.txt" content into "journal_copie.txt"

# we will use shutil module 

import shutil

source = "TP5_Python/files/journal.txt"
destination = "TP5_Python/files/journal_copie.txt"

try :
    shutil.copyfile(source,destination)
    print(f"content of {source} is copied successfully in {destination} file")
except FileNotFoundError :
    print(f"File {source} not found")


# Move "journal_copie.txt" to a new folder named "archives"

moving_source = destination
moving_dest = "TP5_Python/archives"

try:
    shutil.move(moving_source,moving_dest)
    print(f"file {moving_source} moved successfully to the {moving_dest} directory")
except FileNotFoundError:
    print("file not found")

