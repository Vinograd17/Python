# Task 6
goods = []
features = {'название': '', 'цена': '', 'количество': '', 'единица измерения': ''}
analysis = {'название': [], 'цена': [], 'количество': [], 'единица измерения': []}
n = 0
while True:
    if input('Выход - Q, \nЛюбая клавиша - продолжить: ').upper() == 'Q':
        break
    n += 1
    for i in features.keys():
        user_input = input(f'{i}: ')
        features[i] = int(user_input) if (i == 'цена' or i == 'количество') else user_input
        analysis[i].append(features[i])
    goods.append((n, features.copy()))
    print('Аналитика по товарам:\n ')
    for key, value in analysis.items():
        print(key, value)
