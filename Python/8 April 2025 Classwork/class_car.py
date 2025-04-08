# Машина:
# Должна быть возможность прочитать и записать марку, год выпуска, скорость, расстояние
# Посчитать (в шутку), за какое время машина могла бы пройти это расстояниес указанной скоростью
# Сделать возможность УКАЗАТЬ время, а на самом деле изменить расстояние

class Car:
    def __init__(self, brand, year, speed):
        self.brand = brand
        self.year = year
        self.speed = speed  
        self.distance = 0

    def set_distance(self, distance):
        self.distance = distance

    def get_time_to_travel(self):
        if self.speed > 0:
            time = self.distance / self.speed
            return time
        else:
            return None

    def set_time_and_distance(self, time):
        # Изменяем расстояние на основе указанного времени и текущей скорости
        self.distance = time * self.speed

    def __str__(self):
        return (f"Марка: {self.brand}, Год выпуска: {self.year}, "
                f"Скорость: {self.speed} км/ч, Расстояние: {self.distance} км")


car = Car("Tesla", 2022, 120)
car.set_distance(240)  # Устанавливаем расстояние в 240 км

print(car)
time_to_travel = car.get_time_to_travel()
print(f"Время в пути: {time_to_travel} часов")

car.set_time_and_distance(4)  # Указываем время в 4 часа
print(car)