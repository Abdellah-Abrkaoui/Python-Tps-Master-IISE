# Zero Division Error , else and finally



def safe_division(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        raise ZeroDivisionError("We can not divide by zero")
    else:
        print("The division is successfully done")
        return result
    finally:
        print("Programme end")

try:
    print(safe_division(10, 2))  # valide
    print(safe_division(10, 0))  # exception
except ZeroDivisionError as e:
    print(e)
