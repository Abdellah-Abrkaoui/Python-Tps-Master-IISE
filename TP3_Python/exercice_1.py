# classe de base "Forme"

# l'importation de ABC et abstractmethod du module abc (classes de base abstraites)
from abc import ABC, abstractmethod

class Form(ABC):
    # methode abstraite
    @abstractmethod
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





c1 = Cercle(3)
print(f"la surface de cercle avec le rayon {c1.rayon} est : {c1.calculer_surface()} cm^2")

r1 = Rectangle(10,2)
print(f"la surface de rectangle avec longeur {r1.longeur} et largeur {r1.largeur} est : {r1.calculer_surface()} cm^2")