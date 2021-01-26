# Task 4
class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print('{} is driving!'.format(self.name))

    def stop(self):
        print('{} stops!'.format(self.name))

    def turn(self, direction):
        print('{} turning {}'.format(self.name, direction))

    def show_speed(self):
        print('Current speed: {}'.format(self.speed))


class TownCar(Car):
    def show_speed(self):
        super().show_speed()
        if self.speed > 60:
            print("Warning! You're going too fast")


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        super().show_speed()
        if self.speed > 40:
            print("Warning! You're going too fast")


class PoliceCar(Car):
    pass


town_car = TownCar(70, 'white', 'Maxi', False)
work_car = WorkCar(50, 'blue', 'Work car', False)
sport_car = SportCar(140, 'red', 'Sport car', False)
police_car = PoliceCar(90, 'Red-blue', 'Police car', True)

town_car.show_speed()
work_car.show_speed()
sport_car.stop()
police_car.turn('right')
