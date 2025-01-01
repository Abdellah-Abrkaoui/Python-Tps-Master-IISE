# Statistiques de Fichier

def file_statistics(file_path):
    number_of_lines = 0
    number_of_words = 0
    number_of_characters = 0

    with open(file_path, "r") as file :
        for line in file:
            number_of_lines += 1
            number_of_words += len(line.split())
            number_of_characters += len(line.replace(" ", "").replace("\n", ""))

    print(f"Number of lines: {number_of_lines}")
    print(f"Number of words: {number_of_words}")
    print(f"Number of characters: {number_of_characters}")




my_file = "TP5_Python/files/journal.txt"

try :
    file_statistics(my_file)
except FileNotFoundError :
    print("file not found")



