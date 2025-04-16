# С клавиатуры вводятся целые числа "x". Выводить обратные им (1/x) до возникновения ошибки деления на ноль. 
# Вывести "расчёт окончен" и указать количество введенных чисел.

count = 0

while True:
    try:
        x = int(input("Введите целое число (или 0 для выхода): "))
        if x == 0:
            break
        division = 1 / x
        print(f"Обратное значение {x}: {division}")
        count += 1
    except ValueError:
        print("Ошибка: введите целое число.")
    except ZeroDivisionError:
        print("Ошибка: деление на ноль.")

print(f"Расчёт окончен. Количество введённых чисел: {count}.")
