# Task 3
# через dict
month = int(input('Введите номер месяца от 1 до 12: '))
seasons_dict = {1: 'Winter', 2: 'Winter', 3: 'Spring', 4: 'Spring', 5: 'Spring', 6: 'Summer',
                7: 'Summer', 8: 'Summer', 9: 'Autumn', 10: 'Autumn', 11: 'Autumn', 12: 'Winter'}
print(seasons_dict[month])

# через list

season_list = ['', 'winter', 'winter', 'spring', 'spring', 'spring', 'summer',
               'summer', 'summer', 'autumn', 'autumn', 'autumn', 'winter']
print(season_list[month])
