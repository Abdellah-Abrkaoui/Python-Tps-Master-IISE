#  Classe "Vehicule" avec Méthodes Abstraites

from abc import ABC, abstractmethod

class Vehicule(ABC):

    # methode abstraite deplacer()
    @abstractmethod
    def deplacer(self):
        pass


class Voiture(Vehicule):

    def deplacer(self):
        print("la voiture est deplacer")



class Bicyclette(Vehicule):

    def deplacer(self):
        print("Bicyclette est deplacer")




v1 = Voiture()
v1.deplacer() # la voiture est deplacer

b1 = Bicyclette()
b1.deplacer() # Bicyclette est deplacer