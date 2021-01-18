# Task 1
from sys import argv

script_name, wages, working_hours, premium = argv


def salary(param_1, param_2, param_3):
    total = param_1 * param_2 + param_3
    return total


print('Your salary is: ', salary(int(wages), int(working_hours), int(premium)))
