#1: Создать список и проверить тип данных
my_list = [1, 2, 3, 4, 5, "name", 13.2, "over", -145]
print(my_list)
for x in my_list:
    print(type(x))

# Реализация обмена
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