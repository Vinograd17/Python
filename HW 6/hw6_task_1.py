# Task 1
import time


class TrafficLight:
    def __init__(self):
        self._color_1 = 'red'
        self._color_2 = 'yellow'
        self._color_3 = 'green'

    def running(self):
        print(self._color_1)
        time.sleep(7)
        print(self._color_2)
        time.sleep(2)
        print(self._color_3)
        time.sleep(5)


traffic_light = TrafficLight()
traffic_light.running()
