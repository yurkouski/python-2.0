#1 Расчет заработной платы:
from sys import argv
def result():
    try:
        bid = int(input('Ваша ставка в часах: '))
        working_hours = int(input('Ваша выробатка в часах: '))
        bonus = int(input('Введите премию: '))
        salary = working_hours * bid + bonus
        print(f"Здравствуйте, вы заработали {salary}!")
    except ValueError:
        return(print('Вы ввели некорректные данные'))

result()

#2 Список
list_1 = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
my_list = [el for num, el in enumerate(list_1) if list_1[num - 1] < list_1[num]]
print(f'Исходный список: {list_1}')
print(f'Новый список: {my_list}')

#3 Кратные числа
my_list = [el for el in range(20, 240) if el % 20 == 0 ]

print(my_list)

#4 Определить элементы списка

list_1 = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
my_list = [el for el in list_1 if list_1.count(el) == 1]
print(f'Исходный список: {list_1}')
print(f'Новый список: {my_list}')

#5 Реализовать формирование списка
from functools import reduce
my_list = [el for el in range(99, 1001) if el % 2 == 0]
print(reduce(lambda x, y: x * y, my_list))
