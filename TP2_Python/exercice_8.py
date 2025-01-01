#  Classe "Personne" avec Gestion d'Amis

# création de la classe Personne

class Personne():

    # constructeur
    def __init__(self,nom,prenom,age):
        self.nom = nom
        self.prenom = prenom
        self.age = age
        self.amis = []

    # affichage d'une présentation de la personne
    def se_presenter(self):
        print(f"nom est : {self.nom}, prenom est : {self.prenom}, age est : {self.age}")
    
    # methode pour ajouter un ami a la liste
    def ajouter_ami(self,ami):
        if ami not in self.amis:
            self.amis.append(ami)
            print(f"{ami} est ajoute a la liste des amis")
        else:
            print(f"{ami} est deja existe dans la liste des amis")

    # methode pour afficher la liste des amis
    def afficher_amis(self):
        if self.amis:
            print(f"la liste des amis : ")
            for ami in self.amis:
                print(f"--{ami}")
        

    


# Création des instances de la classe Personne

p1 = Personne("abdellah","abrkaoui",21)
p1.se_presenter() # nom est : abdellah, prenom est : abrkaoui, age est : 21


# 

p1.ajouter_ami("mohamed") # mohamed est ajoute a la liste des amis
p1.ajouter_ami("achraf") # achraf est ajoute a la liste des amis

p1.afficher_amis() 

"""
resultat :

la liste des amis :
--mohamed
--achraf

"""


