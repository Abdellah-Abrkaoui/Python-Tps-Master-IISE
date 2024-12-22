#  Classe "Personne" avec Encapsulation


# Premier Methode : Sans utiliser @property
class Personne():
    # constructor
    def __init__(self,nom,prenom,age):
        self.__nom = nom
        self.__prenom = prenom
        self.__age= age

    # getters
    def getNom(self):
        return self.__nom

    def getPrenom(self):
        return self.__prenom

    def getAge(self):
        return self.__age
    
    # setters
    def setNom(self,newName):
        self.__nom = newName
    
    def setPrenom(self,newPrenom):
        self.__prenom = newPrenom
    
    def setAge(self,newAge):
        if newAge>0:
            self.__age = newAge
        else:
            print("age doit etre positif")
            



p1 = Personne("abdellah","abrkaoui",22)
print(p1.getNom()) #Abdellah
p1.setNom("Houcine")
print(p1.getNom()) #Houcine
p1.setAge(-1) # age doit etre positif


print("*"*50)


# Deuxieme Methode : Avec utiliser @property


class Perso():

    def __init__(self,nom,prenom,age):
        self.__nom = nom
        self.__prenom = prenom
        self.__age= age
    
    @property
    def nom(self):
        return self.__nom
    
    @nom.setter
    def nom(self,newNom):
        self.__nom = newNom

    
    @property
    def prenom(self):
        return self.__prenom

    @prenom.setter
    def prenom(self,newPrenom):
        self.__prenom = newPrenom
    
    
    @property
    def age(self):
        return self.__age
    
    @age.setter
    def age(self,newAge):
        if newAge>0:
            self.__age = newAge
        else:
            print("age doit etre positif")



p2 = Perso("ali","almouden",22)
print(p2.nom) #ali
print(p2.prenom) #almouden
print(p2.age) #22
p2.age = 26
print(p2.age) #26


        