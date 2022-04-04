#1 Реализовать функцию
def r_calc():
    while True:
        try:
            x = float(input("Введите  любое число: "))
            y = float(input("Введите  еще одно любое число: "))
            result = x / y
            return result
        except ZeroDivisionError:
            print("На ноль делить нельзя")

res = r_calc()
print(res)

#2 Выполнить функцию, которая принимает несколько параметров
def user_def():
    name = input('Введите ваше имя: ')
    surname = input('Введите вашу фамилию: ')
    age = input('Введите дату рождения')
    cyti = input('Где вы проживаете: ')
    email = input('Введите вашу почту: ')
    telephone = input("Введите выш телефон: ")
    return(f"Данные пользователя: {name}, {surname}, {age} г.р., проживающий в г. {cyti}, {email}, {telephone} ")

print(user_def())

# 3 Задание
def my_func(a, b, c):
    if a >= b >= c:
        x = a + b
    elif a >= c >= b:
        x = a + c
    elif b >= a >= c:
        x = b + a
    elif b >= c >= a:
        x = b + c
    elif c >= a >= b:
        x = c + a
    elif c >= b >= a:
        x = c + b
    return(x)

print(f"Результат: {my_func(int(input('Введите 1 значение: ')), int(input('Введите второе значение: ')), int(input('Введите третье значение: ')))} ")

# 4 Возведение в степень
def my_func():
    while True:
        try:
            x = float(input('Введите положительное число: '))
            y = int(input('Введите отрицательное число: '))
            z = x ** y
            return z
        except ValueError:
            print("Ввели неправильное число")

print(f'Результат: {my_func()} ')

#5 Запрос на строку чисел:
def my_func():
    my_list = input("Введите набор чисел разделенных пробелом: ").split()
    thesum = 0
    a = 'stop'
    for i in my_list:
        thesum = thesum + int(i)
    print(thesum)
    while True:
        my_list.append(input('Введите следующее число, если нет, напишите stop: '))
        z = my_list[-1]
        if a == z:
            my_list.remove("stop")
            break
        elif a != z:
            thesum = thesum + int(my_list[-1])
            print(thesum)
    return (thesum)
print("Результат: " + str(my_func()))


#6 Прописная первая буква
def my_func():
    my_list = input('Введите предложение с маленькой буквы: ')
    my_list2 = str.capitalize(my_list)
    return my_list2

print(f'Результат: {my_func()}')

#7 В каждом слове заглавная буква
def my_func():
    my_list = input('Введите предложение с маленькой буквы: ')
    my_list2 = str.title(my_list)
    return my_list2

print(f'Результат: {my_func()}')