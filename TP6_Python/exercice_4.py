# Exception personnalise

class NegativeAgeError(Exception):
    def __init__(self,age):
        super().__init__("L'age est negative")


def set_age(age):
    if age < 0:
        raise NegativeAgeError(age)
    print(f"l'age que vous definie est {age}")


try:
    print(set_age(-19)) # L'age est negative
    # print(set_age(19)) # l'age que vous definie est 19

except NegativeAgeError as e :
    print(e)