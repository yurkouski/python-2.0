a = int(input("Сколько вы пробежали в первый день: "))
b = int(input("Какой результат хотелось бы: "))
days = 1
km = a
while km < b:
    x = a + (0.1 * a)
    days = days + 1
    km = km + x
print("Вы достигнете результата через " + str(days))
