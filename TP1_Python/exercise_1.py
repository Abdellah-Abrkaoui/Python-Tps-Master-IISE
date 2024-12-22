# exercise : sum of a list


# version 1
def sum_of_list(myList):
    total = 0
    for i in range(len(myList)):
        total+=myList[i]
    return total


#Test

testList = [1,2,3,4,5,6,7]
result = sum_of_list(testList)

print("sum of items in that list" ,testList ,"is",result)


# version 2 using build in function sum()

def sum_of_list_v2(list):
    return sum(list)


print(sum_of_list_v2([1,2,4]))




