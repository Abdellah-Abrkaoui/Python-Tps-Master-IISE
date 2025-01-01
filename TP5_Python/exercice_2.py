# Écriture dans un Fichier


def write_file(file,listOfPhrases):
    with open(file, "w") as file :
        for i in listOfPhrases:
            file.write(i+ "\n")


phrases = []
for i in range(1,4):
    ph = input(f"enter sentence {i} : > ")
    phrases.append(ph)



myFile = "TP5_Python/files/phrase.txt"
write_file(myFile,phrases)  
print(f"sentences are saved on {myFile} file")      
