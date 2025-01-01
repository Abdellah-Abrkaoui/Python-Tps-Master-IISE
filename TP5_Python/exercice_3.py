# Ajout à un Fichier


def write_file(file,listOfPhrases):
    with open(file, "a") as file :
        for i in listOfPhrases:
            file.write(i+ "\n")


phrases = []
for i in range(1,4):
    ph = input(f"enter sentence {i} : > ")
    phrases.append(ph)

j = 4
while True :
    add_more_sentences = input("Type 'yes' to add more sentences , 'no' otherwise : ").strip().lower()
    if add_more_sentences == "yes":
            ph = input(f"enter sentence {j} : > ")
            phrases.append(ph)
            j += 1
    elif add_more_sentences == "no":
         break
    else :
         print("pls type 'yes' or 'no'")



myFile = "TP5_Python/files/phrase.txt"
write_file(myFile,phrases)  
print(f"sentences are saved on {myFile} file")      
