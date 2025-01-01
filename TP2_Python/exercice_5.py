# Classe "Animal"

# création de la classe Animal "main class"
class Animal():

    def faire_du_bruit(self):
        print("le bruit de l'animle")


# création de la classe Chat "First child class"
class Chat(Animal):

    def faire_du_bruit(self):
        print("le bruit de chat")


# création de la classe Chien "Second child class"
class Chien(Animal):

    def faire_du_bruit(self):
        print("le bruit de Chien")



# Création des instances de la classe Animal et ses sous-classes

animale1 = Animal()
animale1.faire_du_bruit() # le bruit de l'animle


chat1 = Chat()
chat1.faire_du_bruit() # le bruit de chat


chien1 = Chien()
chien1.faire_du_bruit() # le bruit de Chien