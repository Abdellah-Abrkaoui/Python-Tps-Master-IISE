# analyse text and return a dictionary with number of words and numbers of characters


def TextToDict(str):
    myDictionary = {
        "number of words":0,
        "number of characters":0,
    }

    for i in str :
        myDictionary['number of words'] = len(str.split())
        myDictionary["number of characters"] = len(str.replace(" ",""))

    return myDictionary



# test

text = "I love You"


print(TextToDict(text))



    




