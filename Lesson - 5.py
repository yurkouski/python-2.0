#1 Создать програмный фаил

file = open('test.txt', 'w')
line = input('Введите предложение с пробелом вконце: ')
while line:
    file.writelines(line)
    line = input('Введите предложение с пробелом вконце: ')
    if not line:
        break
file.close()
file = open('test.txt', 'r')
f = file.readlines()
print(f)

#2 Выполнить подсчёт строк и слов в каждой строке:
with open(r"C:\Users\Вася\Desktop\test.txt") as file:
    f = file.read()
    print(f)

with open(r"C:\Users\Вася\Desktop\test.txt") as file:
    f = file.read()
    f = f.split()
    f = len(f)
    print("Количество слов:" + str(f))

with open(r"C:\Users\Вася\Desktop\test.txt") as file:
    z = file.readlines()
    z = len(z)
    print("Количество строк:" + str(z))

with open(r"C:\Users\Вася\Desktop\test.txt") as file:
    y = 1
    for line in file:
        x = len(line.split())
        print(f'В {y} строке {x} слова')
        y +=1

# 3 Оклад
with open(r"C:\Users\Вася\Desktop\test.txt") as file:
    few = []
    average = []
    for line in file:
        f = line.split()
        if int(f[1]) < 20000:
            few.append(f[0])
        average.append(f[1])

    print(f'Меньше всех получают {few}, средний оклад всех сотрудников {sum(map(int, average)) / len(average)}')


#4 Текстовый фаил
with open(r"C:\Users\Вася\Desktop\test.txt") as file:
    file = file.read()
    print(file)

with open(r"C:\Users\Вася\Desktop\test.txt") as file:
    my_file = []
    transcript = { 'One': 'один',
                   'Two': 'два',
                   'Three': 'три',
                   'Four': 'четыре' }
    for line in file:
        y = line.split(' ', 1)
        my_file.append(transcript[y[0]] + '-' + y[1])

    print(my_file)

with open(r"C:\Users\Вася\Desktop\test.txt", 'w') as file:
    file.writelines(my_file)