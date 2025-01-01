#  Application Finale

# App functionalities
 
#  1 - we can add contacts to  csv file done
#  2 - we can display all contacts
#  3 - we can search for user contacts
#  4 - we can delete user contacts

import csv

def add_contacts(file_path,contacts):
    with open(file_path, "a") as file :
        file_writer = csv.writer(file)
        file_writer.writerow([contacts["Nom"], contacts["Age"], contacts["Ville"]])


def display_contacts(file_path):
    with open(file_path, "r") as file:
        file_reader = csv.DictReader(file)
        for line in file_reader:
            contact_infos = [f"{key}: {value}" for key, value in line.items()]
            print(", ".join(contact_infos))


def search_contact(file_path,contact_name):
    with open(file_path, "r") as file:
        file_reader = csv.DictReader(file)
        for line in file_reader:
            if line["Nom"].lower() == contact_name :
                print("Contact Found")
                contact_info = [f"{key}: {value}" for key, value in line.items()]
                print(", ".join(contact_info))
                return
            
        print("There is no Contact with that name")


def delete_contact(file_path,contact_name):
    contact_updates = []
    flag = False
    with open(file_path, "r") as file:
        file_reader = csv.DictReader(file)
        headers = file_reader.fieldnames
        for line in file_reader :
            if line["Nom"].lower() == contact_name :
                flag = True # contact exists
                print("deleting Contact ...")
            else :
                contact_updates.append(line)
    if not flag :
        print("Contact Name not found")
        return
    
    # update the file
    with open(file_path, "w") as file :
        file_writer = csv.DictWriter(file, fieldnames=headers)
        file_writer.writeheader()
        file_writer.writerows(contact_updates)





file = "TP5_Python/files/contacts.csv"

print("Welcome to Contact App , Type :")
print("1 - Add Contact")
print("2 - Display All Contacts")
print("3 - Search for a Contact")
print("4 - Delete a Contact")
print("5 - Exit")

while True :

    user_input = int(input("Please select Your Option : "))
    
    if user_input == 1:
        user_name = input("Please Enter Contact Name :")
        user_age = int(input("Please Enter Contact Age :"))
        user_city = input("Please Enter Contact City :")
        
        # store contact infos in dictionary
        contact = {"Nom":user_name, "Age":user_age, "Ville":user_city}
        add_contacts(file,contact)
        print("Contact Added Successfully")


    elif user_input == 2:
        display_contacts(file)
    

    elif user_input == 3:
        searched_name = input("Enter Contact Name You Want To Find : ").lower()
        search_contact(file, searched_name)
    
    elif user_input == 4:
        deleted_contact = input("Enter Contact Name You Want To Delete : ").lower()
        delete_contact(file,deleted_contact)


    elif user_input == 5 :
        print("Exiting the Contact App ....")
        break

    else:
        print("Invalid Command")