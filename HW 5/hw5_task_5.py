# Task 5
with open('text_task_5.txt', 'w', encoding='utf-8') as f_obj:
    nums = str('3 5 6 4 7 5')
    f_obj.write(nums)
    nums = map(int, nums.split())
    sum_nums = sum(nums)
    f_obj.write('\n' + 'Сумма чисел: ' + str(sum_nums))
    print('Сумма введенных чисел: ', sum_nums)
