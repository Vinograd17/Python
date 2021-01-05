my_str = input('Enter several words: ')
line = my_str.split()
for n, word in enumerate(line, start=1):
    print(n, word[:10])
