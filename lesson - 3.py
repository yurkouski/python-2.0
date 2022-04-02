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