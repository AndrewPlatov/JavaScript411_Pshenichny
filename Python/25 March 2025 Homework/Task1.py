# Task 1
# Написать свой класс для хранения информации о человеке: фамилия, имя, отчество, дата рождения

from datetime import datetime

class MenInfo:
    def __init__(self, name, surname, patronymic, year, height):
        self.name = name
        self.surname = surname
        self.patronymic = patronymic
        self.year = year
        self.height = height
    
    def calculate_age(self):
        current_year = datetime.now().year
        return current_year - self.year


mi = MenInfo("Андрей", "Пшеничный", "Михайлович", 1998, 171)

print(mi.name)
print(mi.surname)
print(mi.patronymic)
print(mi.year)
print(mi.calculate_age())