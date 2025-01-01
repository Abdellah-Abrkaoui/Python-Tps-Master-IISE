# Gestion des Erreurs


def file_handling_error(file_path):
    with open(file_path, "r") as file:
        content = file.read()
        print(content)



file = "inexistant.txt"

try :
    file_handling_error(file)
except FileNotFoundError as e:
    print(f"File \"{file}\" not found")