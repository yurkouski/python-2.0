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
    z = line.append(input("Добавьте еще значение, если нет, напишите, stop: "))
    if line[-1] == x:
        line.remove("stop")
        break
        print("Рейтинг: " + str(line))
    elif line[-1] != x:
        line.sort(), line.reverse()
        print("Рейтинг: " + str(line))
        for y in range(len(line)):
            if y == z:
                line[y], line[z] = line[z], line[y]
print("Рейтинг: " + str(line))

