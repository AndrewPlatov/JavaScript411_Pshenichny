# Есть три кортежа целых чисел необходимо найти элементы, которые есть во всех кортежах.

# Берем три кортежа
tuple1 = (1, 2, 3, 4, 5)
tuple2 = (3, 4, 5, 6, 7)
tuple3 = (4, 5, 8, 9)

# С помощью множеств и оператора & найдет общие элементы
commons = set(tuple1) & set(tuple2) & set(tuple3)

print("Общие элементы:", list(commons))