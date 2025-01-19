from src import addition, soustraction, division, multiplication
from src import concat, upper_case
print(addition(1,2))
print(soustraction(1,2))
print(multiplication(1,2))

try:
    print(division(1,0))
except ZeroDivisionError as e:
    print(e)


print(concat('abd','1'))
print(upper_case('abdellah'))



