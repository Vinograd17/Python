# Task 7
from math import factorial
from itertools import count


def fact():
    for el in count(1):
        yield factorial(el)
        

number = 1
for n in fact():
    print('Factorial {} - {}'.format(number, n))
    if number >= 7:
        break
    number += 1
