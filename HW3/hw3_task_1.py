# Task 1

def my_func(var_1, var_2):
    try:
        var_1, var_2 = float(var_1), float(var_2)
        result = round((var_1 / var_2), 2)
    except ValueError:
        return 'You had to enter numbers'
    except ZeroDivisionError:
        return 'Деление на ноль невозможно'
    return result


divided_var = my_func(input('Enter number: '), input('Enter another number: '))
print(divided_var)
