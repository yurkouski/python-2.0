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

#4 Класс Car

class Car:

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return f'{self.name} поехала'
    def stop(self):
        return f'{self.name} остановилась'
    def turn_right(self):
        return f'{self.name} повернула на право'
    def turn_left(self):
        return f'{self.name} повернула на лево'
    def show_speed(self):
        return f'{self.name} едет со скоростью {self.speed} км/ч'

class TownCar(Car):

    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 60:
            print(f'Машина превышает скорость')
        else:
            print(f'Не превышает скорость')

class SportCar(Car):

    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

class WorkCar(Car):

    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 40:
            print(f'Превышает скорость')
        else:
            print(f'Не превышает скорость')

class PoliceCar(Car):

    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

opel = TownCar(100, 'black', "opel", True)
ferrari = SportCar(200, 'red', 'ferrari', True)
belaz = WorkCar(30, 'black', 'belaz', False)
geely = PoliceCar(100, 'withe', 'geely', False)

print(f'{belaz.go()}, после чего {belaz.turn_right()}')
print(opel.show_speed())

