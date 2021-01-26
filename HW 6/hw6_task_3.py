# Task 3
class Worker:
    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        self.income_wage = income['wage']
        self.income_bonus = income['bonus']


class Position(Worker):

    def get_full_name(self):
        return f'{self.name} {self.surname} {self.position}'

    def get_total_income(self):
        return self.income_wage + self.income_bonus


posit = Position('Anton', 'Ivanov', 'CEO', {"wage": 10000, "bonus": 5000})
print(posit.get_full_name())
print(posit.get_total_income())
