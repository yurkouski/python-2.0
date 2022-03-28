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

# Прибыль и издержки
profit = float(input(name + " Сколько вы заработали в этом месяце?:"))
costs = float(input("А сколько вы потеряли в этом месяце: "))
if profit > costs:
    print("Поздравляю, ваша выручка больше издержек")
    staff = float(input ("Сколько у вас работает сотрудников?"))
    revenue = profit - costs
    profitability = profit / revenue
    x = profit / staff
    print("Рентаьелность вашей фирмы равна: " + str(profitability) + " а прибыль на одного сотрудника равна: " + str(x))
elif profit == costs:
    print("Вы вышли по нулям")
elif profit < costs:
    print("Сочувствую, у вас убытков больше чем прибыли")

 # Задание про спортсмена, но чтото я не уверен в нем(
a = int(input("Сколько вы пробежали в первый день: "))
b = int(input("Какой результат хотелось бы: "))
days = 1
km = a
while km < b:
    x = a + (0.1 * a)
    days = days + 1
    km = km + x
print("Вы достигнете результата через " + str(days))
