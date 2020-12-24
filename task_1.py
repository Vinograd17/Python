# # Task 1
a = 100
b = 200
print(a, b, sep=', ')

name = input('Введите ваше имя: ')
age = int(input('Введите ваш возраст: '))

print(name, age, sep=', ')

# # Task 2
time = int(input('Введите время в секундах: '))
hours = time // 3600
hours_left = time % 3600
minutes = hours_left // 60
minutes_left = hours_left % 60
seconds = minutes_left % 60

print(f"{hours:02}:{minutes:02}:{seconds:02}")

# Task 3
num = input('Введите число: ')
print(f"{num} + {num + num} + {num + num + num} = {int(num) + int(num + num) + int(num + num + num)}")

# Task 4
n = int(input('Введите целое положительное число: '))
max_n = 0

while n > 0:
    last_num = n % 10
    if last_num > max_n:
        max_n = last_num
        if max_n == 9:
            break
    n = n // 10

print(f'Наибольшая цифра в числе: ', max_n)

# Task 5
rev = int(input('Введите значение выручки: '))
costs = int(input('Введите значение издержек: '))
profit = rev - costs
ros = rev / costs
if rev > costs:
    print('Ваша компания прибыльна!')
    print('Рентабельность выручки: ', ("%.2f" % ((ros - 1) * 100)), '%')
    employees = int(input('Введите численность сотрудников'))
    print('Прибыль на сотрудника составила: ', ("%.2f" % (profit / employees)))
else:
    print('Ваша компания работает в убыток!')

# Task 6
a = int(input('Введите результат пробежки в первый день: '))
b = int(input('Введите желаемый результат пробежки: '))
n = 1
while a < b:
    a = a * 1.1
    n += 1

print('Спортсмен достиг результата не менее - ', b, 'километров на ', n, 'день')
