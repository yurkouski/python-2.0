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