# sum of given numbers using a variadic function


def sum_of_numbers(*args):
    result = 0
    for i in args :
        result+=i
    return result


# Test

print(sum_of_numbers(1,2,3,2))