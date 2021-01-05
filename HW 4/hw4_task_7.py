# Task 7
from math import factorial


def fact(n):
    n = int(input('Enter number: '))
    for el in fact(n):
        yield factorial(n)


print(fact(int(input('Enter number: '))))
