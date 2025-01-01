# exercise > the max of a tuple

def max_tuple(myTuple):
    maximum = myTuple[0]
    for i in range(len(myTuple)):
        if myTuple[i]>maximum:
            maximum = myTuple[i]
    return maximum


#Test

testTuple = (1,2,3,-1)
result = max_tuple(testTuple)
print(result)