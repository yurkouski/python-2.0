#1: Создать список и проверить тип данных
my_list = [1, 2, 3, 4, 5, "name", 13.2, "over", -145]
print(my_list)
for x in my_list:
    print(type(x))

#2 Реализация обмена
a = int(input('Введите количество элементов в вашем списке: '))
my_list_2 = []
b = 0
x = 0
while b < a:
    my_list_2.append(input("Наберите следующий элемент списка: "))
    b += 1
print(my_list_2)
while x < a/2:
    my_list_2[x], my_list_2[x+1] = my_list_2[x+1], my_list_2[x]
    x += 2
print(my_list_2)

#3 Времена года
season = {'3' : "spring", '4' : "spring", '5' : "spring",
          '6' : "summer",'7' : "summer", '8' : "summer",
          '9' : 'autumn', '10' : "autumn", '11' : "autumn",
          '12' : "winter", '1' : "winter", '2' : "winter"}

month = input("Введите цифру месяца: ")
z = season[month]
print("Вы выбрали время года:" + z + "!")

#4 Пользователь вводит строку
line_1 = input("Введите предложение из нескольких строк с пробелами: ").split()
print(line_1)
i = 0
for word in line_1:
    i += 1
    word.count("")
    b = word.count("")
    if b <= 10:
        print(i, word)
    else:
        print(i, word[0:10])

#5 Рейтинг
line = list(input("Введите любое количество натуральных чисел: "))
line.sort(), line.reverse()
print("Рейтинг: " + str(line))
x = "stop"
while line[0] != x:
    line.append(input("Добавьте еще значение, если нет, напишите, stop: "))
    z = line[-1]
    q = z
    if z == x:
        line.remove("stop")
        break
        print("Рейтинг: " + str(line))
    elif z != x:
        line.sort(), line.reverse()
        print("Рейтинг: " + str(line))
        for namber in range(len(line)):
            if namber == q:
                y = line.index(q)
                if line[y] >= q and q > line[y+1]:
                    line.insert(y, y+1) # Не получилось сделать перенос элемента правее(((
print("Рейтинг: " + str(line))

