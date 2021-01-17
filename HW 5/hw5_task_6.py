# Task 6
my_dict = dict()

with open('text_task_6.txt', encoding='utf-8') as f_obj:
    lines = f_obj.readlines()
for line in lines:
    split_line = line.split()
    my_var = split_line[0]
    sum_of_hours = sum([int(x[:x.find('(')]) for x in split_line[1:] if '(' in x])
    my_dict[my_var[:-1]] = sum_of_hours
print(my_dict)
