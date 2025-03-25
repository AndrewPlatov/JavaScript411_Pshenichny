# Задача: посчитать, сколько дней осталось до вашего дня рождения.
# А сколько часов?

# Для начала нужно импортировать datetime
from datetime import datetime

# Далее указываем интересующую дату рождения
birthday = datetime(1998, 6, 2, 14, 0)

# Присваиваем текщее время
now = datetime.now()

# Устанавливаем дату следующего дня рождения
# {replace() не изменяет исходный объект, а возвращает новый объект}
next_birthday = birthday.replace(year=now.year)

# Если день рождения уже прошел в этом году, устанавливаем на следующий год
if now > next_birthday:
    next_birthday = next_birthday.replace(year=now.year + 1)

# Вычисляем разницу во времени до дня рождения
time_until_birthday = next_birthday - now

# Получаем количество дней и часов до дня рождения
days_until_birthday = time_until_birthday.days
hours_until_birthday = time_until_birthday.seconds // 3600 

print(f"Дней до следующего дня рождения: {days_until_birthday}")
print(f"Часов до следующего дня рождения: {hours_until_birthday}")

print()
print('Прошло ', datetime.now() - birthday)