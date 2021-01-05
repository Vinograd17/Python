# Task 3
def my_func(var_1, var_2, var_3):
    list_1 = [var_1, var_2, var_3]
    min_1 = min(list_1)
    list_1.pop(list_1.index(min_1))
    sum_of_max = sum(list_1)
    return sum_of_max


print(my_func(int(input('Введите число: ')), int(input('Введите число: ')), int(input('Введите число: '))))
