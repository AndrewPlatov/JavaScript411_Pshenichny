# Task 1
# Написать свой класс для хранения информации о человеке: фамилия, имя, отчество, дата рождения

class MenInfo:
    name = "Андрей"
    surname = "Пшеничный"
    pathronymic = "Михайлович"
    year = 1998
    month = 3
    day = 2
    hour = 14
    minute = 0
    second = 0
    
mi = MenInfo()
print(mi.name)
print(mi.surname)
print(mi.pathronymic)
print(mi.year)
print(mi.hour)
print(mi.minute)
print(mi.second)

print()
# ------------------------------------------------------------------------------------------------------------------ #

# Task 2
# Написать свой класс для хранения информации об автомобиле: фирма, модель, год выпуска, объем двигателя, цвет

class CarInfo:
    brand = "Tesla"
    model = "Model Y"
    year = 2025
    engine = "Electric"
    horsepower = "188 to 274 kW"
    color = "Grey"
    
ci = CarInfo()
print(ci.brand)
print(ci.color)
print(ci.engine)
print(ci.horsepower)
print(ci.model)

print()
# ------------------------------------------------------------------------------------------------------------------ #
# Написать свой класс для хранения информации о единице одежды: тип, фирма, цвет

class ClothInfo:
    def __init__(self, form="T-shirt", brand="Nike", color="Red", amount=10):
        self.form = form
        self.brand = brand
        self.color = color
        self.amount = amount
        
cin = ClothInfo()
print(cin.amount, cin.form, cin.color)
# ------------------------------------------------------------------------------------------------------------------ #