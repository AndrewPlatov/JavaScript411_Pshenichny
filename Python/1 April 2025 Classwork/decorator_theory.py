# Идея декоратора

# def get_number_from_user():
#     return int(input('Введите число: '))
# answer = None
# try:                                    # отсюда пошло исключение
#     answer = get_number_from_user()
# except:
#     print('Это не число...')

# ! Каждый раз при использовании функции get_number_from_user придётся использовать подобную конструкцию.

# --------------------------------------------------------------------------------------------------------------- #

# Функцию можно присвоить переменной. Переменная становится "вызываемой" (callable) - это можно проверить 
# с помощью функции проверки или просто вызвать переменную, которая теперь функция.

# печать = print
# печать("Я умею печатать")
# callable(печать) # проверка что печать является функцией 

# --------------------------------------------------------------------------------------------------------------- #

# Измеряем время

# Пусть есть функция, которая выполняется долго. Т.е. не мгновенно, а
# несколько секунд

# # Декоратор - КАК? Шаг 1
# from datetime import datetime, timezone

# def measure_time():
#     dt_start = datetime.now(timezone.utc)
#     multiplication()
#     dt_end = datetime.now(timezone.utc)
#     print(dt_end - dt_start)
    
# # Теперь есть способ измерить время работы... РОВНО ОДНОЙ ФУНКЦИИ. 
# # Будет ли отличаться измерение времени для других функций? НЕТ!

# def multiplication():
#     for i in range(10**8):  # 100 миллионов умножений
#         6.9 * 7.3
#     print('Долгая функция закончилась')
#     return 789

# measure_time()

# --------------------------------------------------------------------------------------------------------------- #

# Раз функцию можно присвоить в переменную, её можно передать в качестве параметра. 
# Теперь наш измеритель времени можем измерить время работы любой функции

# def multiplication():
#     for i in range(10**8):  # 100 миллионов умножений
#         6.9 * 7.3
#     print('Долгая функция закончилась')
#     return 789

# from datetime import datetime, timezone

# def measure_time(func):
#     dt_start = datetime.now(timezone.utc)
#     func()
#     dt_end = datetime.now(timezone.utc)
#     return dt_end - dt_start
    
# def division():
#     for i in range(3 * 10**8):  
#         234.6/287.2
#     print('С вами была функция деления. До новых встреч!')

# print(measure_time(multiplication))
# print(measure_time(division))

# --------------------------------------------------------------------------------------------------------------- #

# # убедиться, что multi - это функция

# from datetime import datetime, timezone

# def multiplication():
#     for i in range(10**8):
#         6.9 * 7.3
#     print('Долгая функция закончилась')
#     return 789

# def measure_time(func):
#     def better_func():
#         dt_start = datetime.now(timezone.utc)
#         func()
#         dt_end = datetime.now(timezone.utc)
#         print(dt_end - dt_start)
#     return better_func
# multi = measure_time(multiplication)
# print(multi()) 

# print(callable(multiplication)) 

# --------------------------------------------------------------------------------------------------------------- #

from datetime import datetime, timezone

def measure_time(func):
    def better_func(*args, **kwargs):
        dt_start = datetime.now(timezone.utc)
        result = func(*args, **kwargs)
        dt_end = datetime.now(timezone.utc)
        print(f"Время выполнения: {dt_end - dt_start}")
        return result
    return better_func

@measure_time
def multiplication(ten_degree):
    for i in range(10**ten_degree):
        6.9 * 7.3 
    print('Долгая функция закончилась')
    return 789

multiplication(20)
