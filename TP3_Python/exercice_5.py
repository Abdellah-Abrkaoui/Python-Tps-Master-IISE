# Classe "Employe" et Sous-classe "Manager"

class Employe():

    def __init__(self,nom,prenom,salaire):
        self.nom = nom
        self.prenom = prenom
        self.salaire = salaire
    
    def afficher_details(self):
        print(f"L'employee {self.nom} {self.prenom} qui a le salaire {self.salaire}")

        
class Manager(Employe):

    def __init__(self, nom, prenom, salaire):
        super().__init__(nom, prenom, salaire)
        self.employees = []
    

    def ajouter_employees(self,employe):
        self.employees.append(employe)
    
    def afficher_employees(self):
        if self.employees:
            print(f"La liste des Employees manager par le manager {self.nom} est :")
            for emp in self.employees:
                emp.afficher_details()
        else:
            print(f"aucun employee est manager par {self.nom}")


emp1 = Employe("ali","alouai",1200)
emp2 = Employe("med","alouai",200)
emp3 = Employe("marwane","alouai",1100)
emp4 = Employe("marwane","alouai",100)

manager1 = Manager("abdellah","abrkaoui",12000)

manager1.ajouter_employees(emp1)
manager1.ajouter_employees(emp2)
manager1.ajouter_employees(emp3)
manager1.ajouter_employees(emp4)
manager1.afficher_employees()

"""
resultat :

La liste des Employees manager par le manager abdellah est :
L'employee ali alouai qui a le salaire 1200
L'employee med alouai qui a le salaire 200
L'employee marwane alouai qui a le salaire 1100
L'employee marwane alouai qui a le salaire 100

"""
print("*"*50)
manager2 = Manager("houcine","ab",22000)
manager2.afficher_employees() # aucun employee est manager par houcine



