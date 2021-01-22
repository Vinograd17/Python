# Task 5
class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Drawing started')


class Pen(Stationery):
    def draw(self):
        print('Writing started')


class Pencil(Stationery):
    def draw(self):
        print('Picture is being painted')


class Handle(Stationery):
    def draw(self):
        print('A word is underlined')


pen = Pen('Lord')
pencil = Pencil('Castle')
handle = Handle('Crown')

pen.draw()
pencil.draw()
handle.draw()
