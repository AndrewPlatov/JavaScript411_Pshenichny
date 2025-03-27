# С помощью магического метода str научить печататься свои классы.
# Например, класс "автомобиль"

# Часть взял из домашки:

# class CarInfo:
#     brand = "Tesla"
#     model = "Model Y"
#     year = 2025
#     engine = "Electric"
#     horsepower = "188 to 274 kW"
#     color = "Grey"
    
class CarInfo:
    def __init__(self, brand, model, year, engine, horsepower, color):
        self.brand = brand
        self.model = model
        self.year = year
        self.engine = engine
        self.horsepower = horsepower
        self.color = color

    def __str__(self):
        return (f"Автомобиль:\n"
                f"Марка: {self.brand}\n"
                f"Модель: {self.model}\n"
                f"Год выпуска: {self.year}\n"
                f"Двигатель: {self.engine}\n"
                f"Мощность: {self.horsepower}\n"
                f"Цвет: {self.color}")

car = CarInfo(brand="Tesla", model="Model Y", year=2025, engine="Electric", horsepower="188 to 274 kW", color="Grey")

print(car)