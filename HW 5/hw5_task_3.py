# Task 3
with open('salary_text_task_3.txt', 'r', encoding='utf-8') as f_obj:
    n = 0
    sum_salary = 0
    for line in f_obj:
        n += 1
        sum_salary = sum_salary + float(line.split(': ')[1])
        if float(line.split(': ')[1]) > 20000:
            print(line)
    print('Средняя зарплата равна: ', "{:.2f}".format(sum_salary / n))
