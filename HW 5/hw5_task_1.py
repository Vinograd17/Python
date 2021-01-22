# Task 1
with open('my_file.txt', 'w') as f_obj:
    while True:
        if input('To stop enter "q", any other letter to continue: ') == 'q':
            break
        line = input('Enter text: ')
        print(line, file=f_obj)
