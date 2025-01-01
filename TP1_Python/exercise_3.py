# exercise 3 > merge two sets

#First method

"""
def merge_sets(mySet_1, mySet_2):
    globalSet = mySet_1.copy()
    for i in mySet_2:
        if i not in globalSet :
            globalSet.add(i)
    return globalSet



#Test

set_1 = {1,2,3,'A'}
set_2 = {4,5,6,'B'}

result_1 = merge_sets(set_1,set_2)

print(result_1)

"""

## Second Method > using union build in function or |

def merge_sets_using_union(s1,s2):
    #globalS = s1.union(s2)
    globalS = s1 & s2
    return globalS


set_3 = {1,2,3,'A'}
set_4 = {4,2,6,'B'}

result_2 = merge_sets_using_union(set_3,set_4)

print(result_2)