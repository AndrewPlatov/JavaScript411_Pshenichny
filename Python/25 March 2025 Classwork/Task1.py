# Задача: посчитать, сколько дней осталось до вашего дня рождения.
# А сколько часов?

from datetime import datetime

birthday = datetime(1998, 6, 2, 14, 0)

now = datetime.now()

next_birthday = birthday.replace(year=now.year)

if now > next_birthday:
    next_birthday = next_birthday.replace(year=now.year + 1)

time_until_birthday = next_birthday - now

days_until_birthday = time_until_birthday.days
hours_until_birthday = time_until_birthday.seconds // 3600 

print(f"Дней до следующего дня рождения: {days_until_birthday}")
print(f"Часов до следующего дня рождения: {hours_until_birthday}")
