#  Gestion de Produits avec Encapsulation

# classe "Produit"

class Produit():

    def __init__(self,nom,prix):
        self.__nom = nom
        self.__prix = prix
        self.remise = 10
        self.seuil_de_remise = 2000

    def appliquer_remise(self):
        if self.__prix > self.seuil_de_remise:
            self.__prix -= self.__prix * (self.remise / 100)
        
    
    def afficher_details(self):
        print(f"Le produit {self.__nom} , prix {self.__prix}$")

              





p1 = Produit("Iphone 13",30000)
p2 = Produit("chargeur",30)

# avant l'application de remise 
print("######### Avant le remise ############")
p1.afficher_details() # Le produit Iphone 13 , prix 30000$
p2.afficher_details() # Le produit chargeur , prix 30$


print("######### Apres le remise ############")
# apres l'application de remise de 10% si prix de produit est depasse 2000$
p1.appliquer_remise()
p2.appliquer_remise()

p1.afficher_details() # Le produit Iphone 13 , prix 27000.0$
p2.afficher_details() # Le produit chargeur , prix 30$ 

