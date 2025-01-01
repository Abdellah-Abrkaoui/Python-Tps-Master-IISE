# Système de Gestion de Transport


# Classe "Vehicule"
class Vehicule():

    def __init__(self,marque,model,annee):
        self.marque = marque
        self.model = model
        self.annee = annee

    
    def afficher_info(self):
        print(f"Vehicule --> marque : {self.marque} , model : {self.model}, annnee de fabrication : {self.annee}")



# Classe "Moteur"
class Moteur():

    def __init__(self,puissance,type_moteur):
        self.puissance = puissance
        self.type_moteur = type_moteur
        
    
    def afficher_mouteur(self):
        print(f"puissance de mouteur est : {self.puissance} cheveaux , type de moteur : {self.type_moteur}")



# Classe "Voiture"
class Voiture(Vehicule, Moteur):

    def __init__(self,marque,model,annee,puissance,type_moteur,nombre_de_places):
        Vehicule.__init__(self,marque,model,annee)
        Moteur.__init__(self,puissance,type_moteur)
        self.nombre_de_places = nombre_de_places
    
    def afficher_info(self):
        super().afficher_info()
        self.afficher_mouteur()
        print(f"nombre de places : {self.nombre_de_places}")

# Classe "Moto"

class Moto(Vehicule, Moteur):

    def __init__(self, marque, model, annee,puissance,type_moteur,type_moto):
        Vehicule.__init__(self,marque, model, annee)
        Moteur.__init__(self,puissance,type_moteur)
        self.type_moto = type_moto


    def afficher_info(self):
        super().afficher_info()
        self.afficher_mouteur()
        print(f"type de moto : {self.type_moto}")










# instanciation


v1 = Voiture("BMW","model 2020",2020,150,"disel",6)
m1 = Moto("Yamaha","model 2020",2020,200,"disel","Sport")

v1.afficher_info()
m1.afficher_info()
    
# print(Moto.mro())

    
    
    


