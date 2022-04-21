#1 Задание. Реализовать класс дата:
class Date:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    def __str__(self):
        return f'Дата: {str(self.day)}/{str(self.month)}/{str(self.year)}'

    @classmethod
    def number(cls, data):
        my_data = []
        for i in data.split():
            my_data.append(i)
        return (f'Числа: {int(my_data[0]),int(my_data[1]), int(my_data[2]) }')

    @staticmethod
    def valid(day, month, year):
        if 1 <= day <= 31 and 1 <= month <= 12 and 1990 <= year <= 2022:
                    return (f' Дата написана правильно')
        else:
            return (f'Дата написана неправильно')

a = Date(10, 10, 10)
print(a)
print(Date.number('10 10 10'))
print(Date.valid(10, 10, 2023))

# 2 задание Класс исключение:

class My_class:
    def __init__(self, param_1, param_2):
        self.patam_1 = param_1
        self.param_2 = param_2

    def func(self):
            try:
                return f'{self.patam_1 / self.param_2}'
            except:
                return f'Деление на ноль недопустимо'

            return f'Результат: {self.patam_1 / self.param_2}'

a = My_class(20, 10)
print(a.func())

# 3 задание Класс исключение, проверяющий содержимое списка:
class Error:
    def __init__(self, *args):
        self.my_list = []

    def my_func(self):
        while True:
            try:
                a = int(input("Введите число: "))
                self.my_list.append(a)
                print(self.my_list)
            except:
                print('Недопустимое значение')
                yes_no = input(f'Продолжить ввод числа: yes/no')

                if yes_no == 'yes':
                    print(try_except.my_func())
                    break
                elif yes_no == 'no':
                    print('Вы вышли')
                else:
                    print('Вы вышли')
                    break

try_except = Error()
print(try_except.my_func())

# 4-6 Оргтехника:

class Stock:
    stock_count = 0
    def __init__(self, name, price, quantity, number, *args):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.number = number
        self.my_stock = []
        self.unit = {'имя техники': self.name,
                     'цена за устройство' : self.price,
                     'количество устройств' : self.quantity}

    def __str__(self):
        return f'Инфорамция о технике: имя - {self.name}, цена - {self.price}, количество - {self.quantity}'


    def reception_stock(self):
        try:
            product = input('Введите имя товара: ')
            product_p = input('Введите цену за товар: ')
            product_q = input('Введите количество: ')
            unit = {'имя техники': product,
                     'цена за устройство' : product_p,
                     'количество устройств' :product_q }
            self.unit.update(unit)
            self.my_stock.append(self.unit)
            print(f'Мой товар: {self.my_stock}')
            Stock.stock_count += 1
        except:
            return f'Неправильно введены данные'

        print(f'Для выхода - stop, продолжение - Enter')
        my_exit = input(f'---> ')
        if my_exit == 'stop':
            print(f' Мой склад: {self.my_stock}')
            return(f'Exit')
        else:
            return Stock.reception_stock

class Printer(Stock):
    def q_print(self):
        return f'Количество данного товара равно: {self.quantity}'

class Xerox(Stock):
    def q_xerox(self):
        return f'Количество данного товара равно: {self.quantity}'

class Scaner(Stock):

    def q_scaner(self):
        return f'Количество данного товара равно: {self.quantity}'

product_1 = Printer('LG', 10, 20, 20)
product_2 = Printer('Sony', 20, 20, 20)
product_3 = Xerox('xerox', 30, 5, 5)
product_4 = Scaner('philips', 5, 5, 5)

print(product_1.reception_stock())
print(product_1.q_print())

# 7 Комплексные числа:
class ComplexNumber:
    def __init__(self, a, b, *args):
        self.a = a
        self.b = b
        self.z = 'a + b * i'

    def __add__(self, other):
        print(f'Сумма классов равна')
        return f'z = {self.a + other.a} + {self.b + other.b} * i'

    def __mul__(self, other):
        print(f'Произведение классов равно')
        return f'z = {self.a * other.a} + {self.b * other.b} * i'

    def __str__(self):
        return f'z = {self.a} + {self.b} * i'


a = ComplexNumber(2, 2)
b = ComplexNumber(4, 4)
print(a)
print(a + b)
print(a * b)