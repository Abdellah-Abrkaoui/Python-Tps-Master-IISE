# Écriture et Lecture de Fichiers JSON

import json

etudiants = {
    "etudiant1": {"nom": "Abdellah", "age": 20, "note": 15},
    "etudiant2": {"nom": "Ali", "age": 22, "note": 18},
    "etudiant3": {"nom": "Mehdi", "age": 21, "note": 16}
}

# store etudiants dict in etudiants.json  or Serialization

# first way > using json.dumps() to convert a Python object into a JSON string
json_file = "TP5_Python/files/file.json"
json_content = json.dumps(etudiants, indent=4)
with open(json_file,"w") as file:
    file.write(json_content)
    

# second way > using json.dump() which directly writes to a JSON file
# with open(json_file, "w") as file :
#     json.dump(etudiants, file,indent=4)


# read a json file or Deserialization
with open(json_file, "r") as file:
    json_content_reader = json.load(file) # json.load() loads the JSON content from a JSON file into a dictionary
    for key, value in json_content_reader.items() :
        print(f"{key}: {value}")


