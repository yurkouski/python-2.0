# Первая домашка
a = 1
print(a)
b = 2
print(b)
c = 3
print(c)

name = input ("Как вас зовут: ")
age = input("Сколько вам лет: ")
print("Приветствую вас " + name + "!")
print("Как здорово, что вам " + str(age) + " лет!")

# Время
time = int(input("Введите время в секундах: "))
hours = time // 3600
minutes = (time - hours * 3600) // 60
seconds = time - (hours * 3600 + minutes *60)
print(str(hours) + ":" + str(minutes) + ":" + str(seconds) + ".")

# Узнать число n
n = int(input("Введите любое число " + name + ":"))
print("Спасибо, что выбрали " + str(n))
total = (n + int(str(n) + str(n)) + int(str(n) + str(n) + str(n)))
print("Мне кажется " + str(total) + " ваше счастливое число")

# Целое положительное число
x = abs(int(input("Введите целое положительное число: ")))
print("Вы выбрали: " + str(x))
m = x % 10
while x > 1:
    x = x // 10
    if x % 10 > m:
       m = x % 10
       x = x // 10
print("Максимальное число: " + str(m))