# Task 5
def sum_of_digits():
    ex = False
    result = 0
    while ex == False:
        digits_line = input('Enter numbers in line separated with whitespaces: '). split()
        digits_result = 0
        for i in digits_line:
            if 'q' in digits_line:
                ex = True
                break
            digits_result += int(i)
        result += digits_result
        print(result)
    return result


print(sum_of_digits())
