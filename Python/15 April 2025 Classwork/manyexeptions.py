# Исключение - работа с нештатной ситуацией try / except

import traceback  # библиотека работы со стеком вызовов
result = 0
znam = int(input('Введите число, я найду обратное:'))
try:
    result = 1 / znam
except ZeroDivisionError:
    print('Я же говорю: не хочу делить на ноль!')
    print(traceback.format_exc())
    result = None
print(result)