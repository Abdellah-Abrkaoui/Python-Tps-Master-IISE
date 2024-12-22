# Classe "Chien"


# création de la classe chien

class Chien():

    # constructeur
    def __init__(self,nom,race,age):
        self.nom = nom        
        self.race = race        
        self.age = age
        print(f"nom de chin est {self.nom} , son race est {self.race} , son age est {self.age}")       


    #  méthode "aboyer" qui affiche "Woof!"
    def aboyer(self):
        print("Woof!")




# Création d'une instance de "Chien" et l'appele de la méthode aboyer
mon_chien = Chien("chien1","race1",10) #nom de chin est chien1 , son race est race1 , son age est 10
mon_chien.aboyer() # Woof!




