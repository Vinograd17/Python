# Task 1
class Matrix:
    def __init__(self, data):
        self.lists = data

    def __str__(self):
        return '\n'.join(' '.join([str(el) for el in line]) for line in self.lists)

    def __add__(self, other):
        result = ''
        for line_1, line_2 in zip(self.lists, other.lists):
            sum_line = [x + y for x, y in zip(line_1, line_2)]
            result += ' '.join([str(i) for i in sum_line]) + '\n'
        return result


matrix_1 = Matrix([[1, 2, 3], [3, 4, 2], [5, 3, 3]])
matrix_2 = Matrix([[2, 4, 2], [5, 7, 2], [5, 9, 2]])
print(matrix_1)
print(matrix_1 + matrix_2)
