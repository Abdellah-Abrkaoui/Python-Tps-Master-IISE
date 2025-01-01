# factoriel bumber using recursive function

# 5! = 5*4*3*2*1

def factorial_recursive(n):
    if n < 0 :
        return "Undefined"
    elif n == 0 or n ==1:
        return 1
    else :
        return n*factorial_recursive(n-1)


# Test

a = -1
print("factoriel of",a,"is ",factorial_recursive(a))





# without recursive
def factoriel(n):
    res = 1
    for i in range(2,n+1):
        res *=i

    return res            
    

#Test
n = 6
print("factoriel of",n,"is ",factoriel(n))