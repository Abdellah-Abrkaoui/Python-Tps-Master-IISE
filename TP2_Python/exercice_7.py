# Gestion de Bibliothèque - classe Livre et Bibliotheque


# classe Livre
class Livre():

    # constructeur
    def __init__(self,titre,auteur,annee_publication):
        self.titre = titre
        self.auteur = auteur
        self.annee_publication = annee_publication

    # methode pour afficher les information d'un livre
    def __str__(self):
        return f"{self.titre} de l'auteur {self.auteur} et de l'anne de pub {self.annee_publication}"
        


# classe Bibliotheque

class Bibliotheque :

    # constructeur
    def __init__(self):
        self.livres = [] # initialisation d'une liste vide pour stocker les livres dans la Bibliotheque
        
    # methode pour ajouter des livres au Bibliotheque
    def ajouter_livre(self,livre):
        self.livres.append(livre)


    # methode pour afficher les livres existent dans le Bibliotheque    
    def afficher_livres(self):
        if len(self.livres)==0:
            print("la Bibliotheque est vide")
        else :
            print("Livres existent dans la Bibliotheque sont :")
            for livre in self.livres:
                print(livre)




# Création des instances de la classe Livre et Bibliotheque

# Création de deux instances de livres
L1 = Livre("mesierable","V Hugo",2000)
L2 = Livre("the compound effect","darwin harry",2010)

# Création d'une instances de Bibliotheque
b1 = Bibliotheque()

# ajoutons les livres au Bibliotheque
b1.ajouter_livre(L1)
b1.ajouter_livre(L2)


b1.afficher_livres()

"""
resultat :

Livres existent dans la Bibliotheque sont :
mesierable de l'auteur V Hugo et de l'anne de pub 2000
the compound effect de l'auteur darwin harry et de l'anne de pub 2010

"""



        