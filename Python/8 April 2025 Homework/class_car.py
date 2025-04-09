# Машина:
# Должна быть возможность прочитать и записать марку, год выпуска, скорость, расстояние
# Посчитать (в шутку), за какое время машина могла бы пройти это расстояниес указанной скоростью
# Сделать возможность УКАЗАТЬ время, а на самом деле изменить расстояние

class Car:
    def __init__(self, brand, year, speed):
        self.__brand = brand
        self.__year = year
        self.__speed = speed  
        self.__distance = 0
        self.__time = 0

    @property
    def brand(self):
        return self.__brand

    @property
    def year(self):
        return self.__year

    @property
    def speed(self):
        return self.__speed

    @property
    def distance(self):
        return self.__distance

    @distance.setter
    def distance(self, value):
        self.__distance = value

    @property
    def time(self):
        return self.__time
    
    @time.setter
    def time(self, value):
        if value >= 0:
            self.__time = value
            self.distance = value * self.speed

    @property
    def time_to_travel(self):
        if self.speed > 0:
            return self.distance / self.speed
        else:
            return None

    def __str__(self):
        return (f"Марка: {self.brand}, Год выпуска: {self.year}, "
                f"Скорость: {self.speed} км/ч, Расстояние: {self.distance} км, "
                f"Время в пути: {self.time} часов")

car = Car("Tesla", 2022, 120)
car.distance = 240  # Устанавливаем расстояние в 240 км

print(car)
print(f"Время в пути: {car.time_to_travel} часов")

car.time = 4  # Указываем время в 4 часа
print(car)