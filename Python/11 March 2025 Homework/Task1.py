# Сделать словарь, ключ - дата, значение - оценка. Оценки сделать случайным образом от 7 до 12.
# Вывести среднюю оценку за весь период.
# Вывести среднюю оценку за УКАЗАННЫЙ период.
# Например, сделайте даты от 1-го января каждый день 20 дней. "за указанный" - это с 4 по 9 января.

import random
from datetime import datetime, timedelta

# timedelta — это класс из модуля datetime в Python, 
# который используется для представления разниц между датами и временем. 
# Он позволяет выполнять математические операции с объектами типа date, time и datetime.

# Генерация дат (год, месяц, день) и случайных оценок
start_date = datetime(2023, 1, 1)
grades = {}

for i in range(20):
    date = start_date + timedelta(days=i)
    grades[date.strftime('%d-%m-%Y')] = random.randint(7, 12)

# Вывод всех оценок
print("Оценки за 20 дней:")
for date, grade in grades.items():
    print(f"{date}: {grade}")

# Рассчет средней оценки за весь период
average_all = sum(grades.values()) / len(grades)

# Форматируем значения переменной. ".2f" означает, что число будет представлено в формате с плавающей точкой (дробное число) 
# с точностью до двух знаков после запятой. Это нужно отображать оценки десятичными знаками.
print(f"\nСредняя оценка за весь период: {average_all:.2f}")

# Указанный период с 4 по 9 января
start_period = datetime(2023, 1, 4)
end_period = datetime(2023, 1, 9)

# Фильтрация оценок за указанный период
grades_in_period = {date: grade for date, grade in grades.items() 
                    if start_period.strftime('%d-%m-%Y') <= date <= end_period.strftime('%d-%m-%Y')}    # Это условие, проверяющее, попадает ли текущая дата date в указанный диапазон между start_period и end_period

# Вывод оценок за указанный период и средней оценки
print("\nОценки за указанный период (04-09 января):")
for date, grade in grades_in_period.items():
    print(f"{date}: {grade}")

if grades_in_period:
    average_period = sum(grades_in_period.values()) / len(grades_in_period)
    print(f"\nСредняя оценка за указанный период: {average_period:.2f}")
else:
    print("\nНет оценок за указанный период.")