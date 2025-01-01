# take a list of words and return it as a dictionary where the keys are words 
# and the value of each key is the number of occurences of that word


def count_occurences(myList):
    myDictionary = {}
    for i in myList:
        myDictionary[i] = myList.count(i)
    return myDictionary

# Test

testList = ["one","two","two","three","three","three"]
result = count_occurences(testList)

print(result)



# without build in function count


def count_occurences_v2(mylist):
    myDict = {}
    for i in mylist:
        if i in myDict:
            myDict[i]+=1
        else:
            myDict[i]=1

    return myDict            


testList_2 = ["one","two","two","three","three","three"]
result_1 = count_occurences_v2(testList_2)

print(result_1)
