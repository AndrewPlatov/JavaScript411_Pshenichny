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

# Task 3
# Написать свой класс для хранения информации о единице одежды: тип, фирма, цвет

class ClothInfo:
    def __init__(self, form="T-shirt", brand="Nike", color="Red", amount=10):
        self.form = form
        self.brand = brand
        self.color = color
        self.amount = amount
        
cin = ClothInfo()
print(cin.amount, cin.form, cin.color)

print()
# ------------------------------------------------------------------------------------------------------------------ #

# Task 4
# Класс Книга: Название, автор, год издания, содержание книги (пример! не надо всю копировать! Можно "Репку" в качестве примера...) 

class Book:
    def __init__(self, name, author, year, briefly, opinion):
        self.name = name
        self.author = author
        self.year = year
        self.briefly = briefly
        self.opinion = opinion

    def display_info(self):
        print(f"Название: {self.name}")
        print(f"Автор: {self.author}")
        print(f"Год издания: {self.year}")
        print(f"Краткое содержание: {self.briefly}")
        print(f"Мнение: {self.opinion}")
        print()

book1 = Book("1984", "Джордж Оруэлл", 1949, "Дистопия о тоталитарном обществе.", "Как лечить алкоголизм курением")
book2 = Book("Война и мир", "Лев Толстой", 1869, "Эпопея о жизни русского общества во время Наполеоновских войн.", "Очень долго, но невероятно захватывает")
book3 = Book("Квантовая механика", "Альберт Месси", 1958, "Основы квантовой механики и её применение в физике.", "Я понял, что я ничего не понял")

print("Информация о книгах:")
book1.display_info()
book2.display_info()
book3.display_info()