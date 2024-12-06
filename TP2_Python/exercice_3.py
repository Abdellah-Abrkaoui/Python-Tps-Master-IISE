# classe "CompteBancaire"


# création de la classe CompteBancaire

class CompteBancaire():

    # constructeur
    def __init__(self,titulaire,solde):
        self.titulaire = titulaire
        self.solde = solde


    # methode pour deposer un montant au compte bancaire 
    def deposer(self,montant):
        if montant > 0:
            self.solde +=montant
            print(f"{montant} est deposer")
        else :
            print("montant doit etre positive")    

    # methode pour retirer de l'argent dasn le compte bancaire 
    def retirer(self,montant):
        if montant>0:
            if self.solde >= montant:
                self.solde -=montant 
                print(f"{montant} est retirer")
            else:
                print("montant insufisant")   
        else:
            print("montant doit etre positive")

    # methode pour afficher le solde d'un compte bancaire
    def afficher_solde(self):
        print(f"Mr/Ms {self.titulaire} a {self.solde} Dh")




# Création des instances de la classe CompteBancaire

compte1 = CompteBancaire("abdellah",1000)
compte1.afficher_solde() # Mr/Ms abdellah a 1000 Dh

compte1.deposer(1000) # 1000 est deposer
compte1.retirer(3000) # montant insufisant

compte1.afficher_solde() # Mr/Ms abdellah a 2000 Dh


        
