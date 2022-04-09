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