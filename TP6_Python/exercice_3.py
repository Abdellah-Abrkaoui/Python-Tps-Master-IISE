# Lecture de ficiher


def read_file(filename):
    file = None
    try:
        file = open(filename, "r") 
        content = file.read()
        return content
    except FileNotFoundError :
        return "File not found"
    finally :
        if file:
            filename.close()
            print("file is closed successfully")



file  = "exemple.txt"
print(read_file(file))