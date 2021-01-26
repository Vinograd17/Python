# Task 2
class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def count_mass(self):
        meter_mass = int(input('Введите массу асфальта для покрытия 1 см дороги: '))
        thickness = int(input('Введите толшину полотна: '))
        print(f"Масса асфальта: {self._width * self._length * meter_mass * thickness}")


road = Road(int(input('Введите длину полотна: ')), int(input('Введите ширину полотна: ')))
road.count_mass()
