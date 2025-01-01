# Traitement de Fichiers CSV

import csv

def read_from_csv(csv_file):

    with open(csv_file,"r") as file:
            
            file_reader = csv.reader(file)
            # store headings in cols
            cols = next(file_reader)

            for row in file_reader:
                contact_infos = []
                for i in range(len(cols)):
                    contact_infos.append(f"{cols[i]}: {row[i]}")
                print(", ".join(contact_infos))
            




my_file = "TP5_Python/files/contacts.csv"

read_from_csv(my_file)