# classe "Rectangle"


# création de la classe Rectangle
class Rectangle():

    # constructeur
    def __init__(self,largeur,hauteur):
        self.largeur = largeur
        self.hauteur = hauteur

    # methode pour calculer la surface du rectangle
    def calculer_surface(self):
        surface = self.largeur * self.hauteur
        print(f"la surface de rectangle avec {self.largeur} en largeur et {self.hauteur} en hauteur est : {surface}")


    # methode pour calculer le périmètre du rectangle
    def calculer_perimetre(self):
        # P=2(l+w)
        P = 2 * (self.largeur + self.hauteur)
        print(f"le perimetre de rectangle avec {self.largeur} en largeur et {self.hauteur} en hauteur est : {P}")




# Création des instances de la classe Rectangle


rec1 = Rectangle(2,4)
rec1.calculer_surface() # la surface de rectangle avec 2 en largeur et 4 en hauteur est : 8
rec1.calculer_perimetre() # le perimetre de rectangle avec 2 en largeur et 4 en hauteur est : 12

        