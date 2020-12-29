# Task 5
my_rating = [7, 5, 3, 3, 2]
user_rating = int(input('Enter number: '))
for index, number in enumerate(my_rating):
    if user_rating <= number:
        continue
    my_rating.insert(index, user_rating)
    break
else:
    my_rating.append(user_rating)
print(my_rating)





