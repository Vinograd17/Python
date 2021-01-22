# Task 2
def data(name, surname, date_of_birth, city, email, phone_number):
    user_data = f"name - {name}; surname - {surname}; date of birth - {date_of_birth}; " \
                f"city - {city}; email - {email}; phone number - {phone_number}"
    return user_data


print(data(name=input('Name: '), surname=input('Surname: '), date_of_birth=input('Date of birth: '),
           city=input('Current city of habitat: '), email=input('Email: '), phone_number=input('Phone number: ')))
