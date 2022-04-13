# Светофор
from time import sleep
class TrafficLight:
    _color = ['Red', 'yellow', 'green']
    def running(self):
        i = 0
        while 3 > i:
            print(f'Цвет светофора: {TrafficLight._color[i]} ')
            if i == 0:
                sleep(7)
            if i == 1:
                sleep(2)
            elif i == 2:
                sleep(3)
            i += 1

a = TrafficLight()
a.running()

# 2 Реализовать класс роад
class Road:
    def __init__(self, lenght, width):
        self._lenght = lenght
        self._width = width

    def massa(self):
        return f'Масса асфальта: {self.lenght * self.width * 25 * 5}'

a = Road(10, 10)
print(a.massa())

#3 Класс Worker

class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        print('Данные сотрудика: ')
        self.name = name
        self.surneme = surname
        self.position = position
        self._income = {'Зарплата': wage, 'Премия': bonus}

class Position(Worker):

    def __init__(self, name, surname, position, wage, bonus ):
        super().__init__(name, surname, position, wage, bonus)

    def get_full_name(self):
        return (f"Полное имя: {self.name} {self.surneme} ")

    def get_total_income(self):
        return (f"Полный оклад: {sum(self._income.values())}")


a = Position('Василий', 'Юрковский', 'хирург', 10, 10)

print(a.get_total_income())