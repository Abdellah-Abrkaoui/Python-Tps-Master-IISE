# classe "Personne"


# création de la classe Personne "main class"

class Personne():

    # constructeur
    def __init__(self,nom,prenom,age):
        self.nom = nom
        self.prenom = prenom
        self.age = age

    # affichage d'une présentation de la personne
    def se_presenter(self):
        print(f"nom est : {self.nom}, prenom est : {self.prenom}, age est : {self.age}")




# création de la classe Etudiant "child class"

class Etudiant(Personne):

    # constructor
    def __init__(self, nom, prenom, age,matricule):
        super().__init__(nom, prenom, age)
        #  ajoutons un attribut "matricule"
        self.matricule = matricule



    # ajoutons une methode etudier
    def etudier(self):
        print(f"la personne avec le matricule {self.matricule} est un etudiant")




# Création des instances de la classe Personne et Etudiant

p1 = Personne("abdellah","abrkaoui",21)
p1.se_presenter() # nom est : abdellah, prenom est : abrkaoui, age est : 21


e1 = Etudiant("med","ab",20,1234)
e1.se_presenter() # nom est : med, prenom est : ab, age est : 20
e1.etudier() # la personne avec le matricule 1234 est un etudiant