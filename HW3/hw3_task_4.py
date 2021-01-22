# Task 4
def my_func():
    x = int(input('Введите целое действительное положительное число: '))
    y = int(input('Введите целое отрицательное число: '))
    result = x * x
    for i in range(2, y):
        result = result * x
    result_1 = 1 / result
    print(result_1)


my_func()
