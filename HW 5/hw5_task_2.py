# Task 2
with open('text_task_2.txt', 'r') as f_obj:
    print('Количество строк в файле: ', len(f_obj.readlines()))

with open('text_task_2.txt', 'r') as f_obj:
    n = 0
    for line in f_obj:
        n += 1
        print('Количество слов в строке', n, ': ', len(line.split(' ')))
