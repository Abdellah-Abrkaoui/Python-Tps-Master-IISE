# classe "Voiture"


# création de la classe Voiture

class Voiture():

    # constructeur
    def __init__(self,marque,model,annee):
        self.marque = marque
        self.model = model
        self.annee = annee

    # affichage des informations de la voiture.
    def afficher_info(self):
        print(f"Voiture {self.marque}, model {self.model}, annee {self.annee}")




# Création des instances de la classe voiture

v1 = Voiture("BMW","X1 SUV",2014)
v2 = Voiture("range rover","sport",2018)



v1.afficher_info() # Voiture BMW, model X1 SUV, annee 2014
v2.afficher_info() # Voiture range rover, model sport, annee 2018

        