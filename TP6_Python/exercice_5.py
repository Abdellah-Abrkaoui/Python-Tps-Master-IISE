# Multi Exceptions


def process_input(user_input):
    try:
        return 10 / user_input
    except ValueError:
        return "Value error : value must be int"
    except ZeroDivisionError:
        return "we can not divide by zero"




userInput = int(input("Enter un nombre : "))
res = process_input(userInput)
print(res)