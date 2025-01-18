# Zero Division Error


def safe_division(a, b):
    if b == 0 :
        raise ZeroDivisionError("we can not divide by zero")
    return a/b


if __name__ == '__main__':


    try:
        print(safe_division(10,2)) 
        print(safe_division(10,0)) 
    except ZeroDivisionError as e:
        print(e)
        


