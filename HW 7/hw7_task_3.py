# Task 3
class Cell:
    def __init__(self, cells_number):
        self.number = cells_number

    def __add__(self, other):
        return str(self.number + other.number)

    def __sub__(self, other):
        return self.number - other.number if self.number - other.number > 0 \
            else 'Your contraction result is below zero'

    def __mul__(self, other):
        return 'Multiplication of cells is: ' + str(self.number * other.number)

    def __truediv__(self, other):
        return str(self.number // other.number)

    def make_order(self, other):
        return '\n'.join(['*' * other for i in range(self.number // other)]) + '\n' + '*' * (self.number % other)


cell_1 = Cell(14)
cell_2 = Cell(13)
print(cell_1.make_order(4))
print(cell_1 - cell_2)
print(cell_1 * cell_2)
print(cell_1 + cell_2)
