def addition(a,b):
    return a + b

def soustraction(a,b):
    return a - b

def multiplication(a,b):
    return a * b

def division(a,b):
    if b == 0:
        raise ZeroDivisionError("Impossible de diviser par zero")
    return a / b