# Polymorphisme

# classe de base "Forme"

class Form():
    def calculer_surface(self):
        pass


class Cercle(Form):

    def __init__(self,rayon):
        self.rayon = rayon
    

    def calculer_surface(self):
        return (self.rayon ** 2) * 3.14
    

class Rectangle(Form):

    def __init__(self,longeur,largeur):
        self.longeur = longeur
        self.largeur = largeur

    

    def calculer_surface(self):
        return self.longeur  * self.largeur


# fonction pour afficher les surfaces des formes d'une liste

def afficher_surface(formes):
    for forme in formes:
        # forme.afficher_surface()
        print(f"la surface est : {forme.calculer_surface()}")
    



formes = [
    Cercle(3),
    Rectangle(10,2),
    Rectangle(10,3)
]


afficher_surface(formes)