# Task 7
from math import factorial


def fact(n):
    yield factorial(n)


total = 1
for el in fact(int(input('Enter a number: '))):
    total = total * el
print(total)
