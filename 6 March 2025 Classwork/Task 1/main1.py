# # Задача 1

# # Создайте три переменных: в одной одно готовое целое число, в другой другое, 
# # а в третьей ответ на вопрос, больше ли первое число второго.

# number1 = 10
# number2 = 5

# is_bigger = number1 > number2
# print(is_bigger)

# # --------------------------------------------------------------------------------------------------------------- #

# # Задача 2

# # Создайте переменную, которая будет знать, равны ли "4" и 4. 
# # Чему она равна? Почему? Какого она типа?

# value = "4" == 4

# print(value)
# print(type(value))

# # --------------------------------------------------------------------------------------------------------------- #

# # Задача 3

# # А теперь создайте переменную, которая хранит сумму числа и строки. 
# # Почему не получилось, кто виноват и что делать ?

# number = 4
# string = "5"

# # Преобразуем строку в целое число
# result = number + int(string)  
# print(result) 

# # --------------------------------------------------------------------------------------------------------------- #

# # Задача 4

# # создайте переменную, которая "не хранит ничего"

# result = None

# # --------------------------------------------------------------------------------------------------------------- #

# # Задача 5

# # Можно ли для хранения скоростей 15 машин на дороге сделать что-то удобнее, чем создать v1, v2...?

# speeds = [60, 70, 80, 55, 65, 75, 90, 85, 50, 100, 95, 40, 45, 110, 120]

# # Можно получить скорость первой машины по ее индексу или любой другой машины по нужному индексу
# print("Скорость первой машины:", speeds[0])

# # Или просто вывести все скорости
# print("Скорости всех машин:", speeds)

# # --------------------------------------------------------------------------------------------------------------- #

# # Задача 6

# letters = set('Мама мыла раму')
# if 'а' in letters: print('Есть такая буква!')

# print(letters)

# # --------------------------------------------------------------------------------------------------------------- #

# # Задача 7

# rainbow = {
#     'violet',
#     'red',
#     'orange',
#     'yellow',
#     'green',
#     'blue',
#     'violet'
# }
# rgb = {'red', 'green', 'blue'}
# print(len(rainbow))

# # --------------------------------------------------------------------------------------------------------------- #

# # # Задача 8

# group321 = {
#     'Ekaterina',
#     'Alex',
#     'Tanya',
#     'Nataly',
#     'Nikolay'
# }

# group411 = {
#     'Sofia',
#     'Andrew',
#     'Arthur',
#     'Konstantin',
#     'Fillip',
#     'Alex'
# }

# # обьединение
# print('All students: ', group321 | group411)

# # пересечение множеств
# print('Перешли: ', group321 & group411)

# # уникальные обьекты
# print('Остались: ', group321 ^ group411)

# # --------------------------------------------------------------------------------------------------------------- #

# Задача 9

# Задайте множество четных чисел от 1 до 10 и множество чисел, делящихся на 3.

n = int(input('Введите значение: '))

even_numbers = {x for x in range(1, n + 1) if x % 2 == 0}

three = {x for x in range(1, n + 1) if x % 3 == 0}

print("Четные числа:", even_numbers)
print("Числа, делящиеся на 3:", three)

# Получите множество чисел, делящихся на 6.

six = {x for x in range(1, n + 1) if x % 6 == 0}

print("Числа, делящиеся на 6:", six)

# --------------------------------------------------------------------------------------------------------------- #
