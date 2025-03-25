# Чтобы использовать дату и время, нужно импортировать их из модуля
from datetime import datetime, timedelta
print(datetime.now())  # new Date() в js
#                   Y     m (1-12) d  Hr  Min
birthday = datetime(1986, 8,       6, 17, 45)  # часы и минуты - необязательно
print('Прошло ', datetime.now() - birthday)
# При вычитании из одной даты другой даты получается timedelta
print(birthday + timedelta(10000))  # по умолчанию состоит из дней
# Прибавить к дате дату нельзя! 
# Что такое "прибавить месяц к 30-му января?"
# Зато можно прибавить timedelta. Он хранит разницу в днях, часах, минутах и секундах

# Можно получить отдельные части даты и времени
print(birthday.year, birthday.month, birthday.day, birthday.hour, birthday.minute)

# Можно получить отдельные части timedelta
td = datetime.now() - birthday
print(td.days, td.seconds)

# как получить часы и мнуты?
# как получить полное количество секунд?
# Задача: посчитать, сколько дней осталось до вашего дня рождения.
# А сколько часов?

print(birthday.strftime('%Y.%m.%d %H:%M'))
exam = datetime.strptime(
    '2025.09.25 19:30', '%Y.%m.%d %H:%M')
