# Task

# Создать свои классы: каждый 4 год високосный. Есть месяцы 31 день, есть 30 дней. Но есть 28 или 29 дней. 
# В зависимости от года и месяца присвоить каждому месяцу количество дней. 
# 100% нужна проверка на високосный год, то есть каждый четвертый. 
# Далее, прописать два варианта: если год високосный, то в феврале 29 дней, если нет, то 28. 
# И для каждого месяца указать в обоих вариантах количество дней.

# ------------------------------------------------------------------ THEORY ---------------------------------------------------------------------------------------- #

# Каждый 4-й год делится на 4 без остатка (self.year % 4 == 0).
# Исключение для 100: Если год делится на 100, он не является високосным, если только он не делится на 400 (self.year % 100 != 0).
# Каждый 400-й год: Год, который делится на 400, является високосным (self.year % 400 == 0).
# Год является високосным, если он делится на 4 и не делится на 100, или если он делится на 400.
    
# 2000 год: Делится на 400, значит, это високосный год.
# 1900 год: Делится на 100, но не на 400, значит, это не високосный год.
# 2020 год: Делится на 4 и не на 100, значит, это високосный год.
# 2021 год: Не делится на 4, значит, это не високосный год.
    
# https://calendar.by/content.php?id=21
# 2032,   2028,   2024,   2020,   2016,   2012,   2008,   2004,   2000,   1996,   1992,   1988,   1984,   1980,   1976,   1972,   
# 1968,   1964,   1960,   1956,   1952,   1948,   1944,   1940,   1936,   1932,   1928,   1924,   1920,   1916,   1912,   1908,   
# 1904,   По григорианскому календарю 1900 - невисокосный год, по юлианскому - високосный.   1896.

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------ #

class Year:
    def __init__(self, year):
        self.year = year


    def is_leap_year(self):
        # Проверка на високосный год
        return (self.year % 4 == 0 and self.year % 100 != 0) or (self.year % 400 == 0)

class Month:
    def __init__(self, name, days):
        self.name = name
        self.days = days

    def __str__(self):
        return f"{self.name}: {self.days} дней"

class Calendar:
    def __init__(self, year):
        self.year = Year(year)
        self.months = self.create_months()

    def create_months(self):
        # Создание списка месяцев високосного года
        if self.year.is_leap_year():
            return [
                Month("Январь", 31),
                Month("Февраль", 29),
                Month("Март", 31),
                Month("Апрель", 30),
                Month("Май", 31),
                Month("Июнь", 30),
                Month("Июль", 31),
                Month("Август", 31),
                Month("Сентябрь", 30),
                Month("Октябрь", 31),
                Month("Ноябрь", 30),
                Month("Декабрь", 31)
            ]
        else:
            # Создание списка месяцев обычного года
            return [
                Month("Январь", 31),
                Month("Февраль", 28),
                Month("Март", 31),
                Month("Апрель", 30),
                Month("Май", 31),
                Month("Июнь", 30),
                Month("Июль", 31),
                Month("Август", 31),
                Month("Сентябрь", 30),
                Month("Октябрь", 31),
                Month("Ноябрь", 30),
                Month("Декабрь", 31)
            ]

    def display_calendar(self):
        print(f"Календарь на {self.year.year} год:")
        for month in self.months:
            print(month)

# Вывод информации о високосном годе
        if self.year.is_leap_year():
            print("Этот год является високосным.")
        else:
            print("Этот год не является високосным.")


year_input = int(input("Введите год: "))
calendar = Calendar(year_input)
calendar.display_calendar()
