# Task 2
from abc import ABC, abstractmethod


class AbstractClothes(ABC):
    def __init__(self, size):
        self.size = size

    @abstractmethod
    def material_usage(self):
        pass


class Coat(AbstractClothes):
    @property
    def material_usage(self):
        return '{:.2f}'.format(self.size / 6.5 + 0.5)


class Costume(AbstractClothes):
    @property
    def material_usage(self):
        return '{:.2f}'.format(2 * self.size + 0.3)


coat = Coat(48)
costume = Costume(7)

print(coat.material_usage)
print(costume.material_usage)
