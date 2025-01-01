# Lecture de Fichiers


def read_file(file):
    with open(file,"r") as file_content:
        line = 1
        for i in file_content:
            print(f"{line} - {i.rstrip()}")
            line+=1

    



myfile = "TP5_Python/files/exemple.txt"
file_content = read_file(myfile)

