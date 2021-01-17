# Task 6
from itertools import count, cycle

for el in count(3):
    if el > 10:
        break
    else:
        print(el)


c = 0
my_list = [1, 2, 3, 4, 5]
for el in cycle(my_list):
    if c > 7:
        break
    print(el)
    c += 1