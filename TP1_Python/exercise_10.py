# merge tw0 dictionaries

def merge_dictionaries(d1,d2):
    globalDict = d1.copy()

    for key,value in d2.items():
        if key in globalDict:
            globalDict[key]+=value
        else:
            globalDict[key] = value

    return globalDict



dict1 = {'a': 10, 'b': 20}
dict2 = {'b': 30, 'c': 40}
result = merge_dictionaries(dict1, dict2)
print(result) 