#  Système de Gestion de Commandes

# Class Produit
class Produit():

    def __init__(self,nom,prix):
        self.nom = nom
        self.prix = prix
    
    def afficher_details(self):
        print(f"Le produit {self.nom} , prix {self.prix}$")



# Class Commande
class Commande():

    def __init__(self,produit,quantite):
        self.produit = produit
        self.quantite = quantite
    
    def total_commande(self):
        return self.produit.prix * self.quantite


    def afficher_Commande(self):
        print(f"Commande : {self.produit.nom} , prix : {self.produit.prix} , Total : {self.total_commande()}")



# Class Panier
class Panier():

    def __init__(self):
        self.commandes = []


    def ajouter_des_commandes(self,commande):
        self.commandes.append(commande)
    

    def total_panier(self):
        totalPanier = 0
        for cm in self.commandes:
            totalPanier += cm.total_commande()
        return totalPanier



        




p1 = Produit("iphone 13",12000)
p2 = Produit("iphone 14",13000)
p3 = Produit("iphone 15",14000)

c1 = Commande(p1,2)
c2 = Commande(p2,1)
c3 = Commande(p3,1)

c1.afficher_Commande() # Commande : iphone 13 , prix : 12000 , Total : 24000
c2.afficher_Commande() # Commande : iphone 14 , prix : 13000 , Total : 13000
c3.afficher_Commande() # Commande : iphone 15 , prix : 14000 , Total : 14000



panier = Panier()
panier.ajouter_des_commandes(c1)
panier.ajouter_des_commandes(c2)
panier.ajouter_des_commandes(c3)

print(f"Le total de panier est {panier.total_panier()}") # Le total de panier est 51000



                      
