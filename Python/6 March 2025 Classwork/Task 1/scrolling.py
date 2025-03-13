# Как просмотреть весь список или кортеж?

# Поэлементно

fruit = {'apple', 'orange', 'avocado'}
for f in fruit:
    print(f)
    print('Длина слова ', f, 'равна', len(f))

# По позиции (тупой, но распространенный вариант)

fruit = ('apple', 'orange', 'avocado')
for i in range(len(fruit)):
    print(i, fruit[i])

# По позиции - супермодный вариант

fruit = ('apple', 'orange', 'avocado')
for i in enumerate(fruit):
    print(i, fruit[i])