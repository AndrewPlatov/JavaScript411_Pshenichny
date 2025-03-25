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