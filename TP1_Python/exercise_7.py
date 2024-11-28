# function with default arguments


def say_Hello(name,message="Hello"):
    print(message+" "+name)


name = "ali"

say_Hello(name)   #Hello Ali
say_Hello(name,"Salut") # Salut Ali


