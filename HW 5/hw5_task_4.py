# Task 4
with open ('text_task_4.txt', encoding='utf-8') as f_obj:
    english = f_obj.readlines()

with open('text_rus_task_4.txt', 'w', encoding='utf-8') as f_obj:
    for line in english:
        if '1' in line:
            line = line.replace('One', 'Один')
        elif '2' in line:
            line = line.replace('Two', 'Два')
        elif '3' in line:
            line = line.replace('Three', 'Три')
        elif '4' in line:
            line = line.replace('Four', 'Четыре')
        f_obj.write(line)
