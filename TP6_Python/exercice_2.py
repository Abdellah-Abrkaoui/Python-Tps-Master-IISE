# type verification

def convert_to_int(value):
    try:
        return int(value)
    except ValueError:
        raise ValueError("La conversion a echoue")
    


if __name__ == '__main__':

    value = "18"
    try:
        print(convert_to_int(value))
    except ValueError as e :
        print(e)

