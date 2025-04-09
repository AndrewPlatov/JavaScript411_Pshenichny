# Треугольник
# Сделать класс треугольник, указав три его стороны
# Треугольник не должен позволять указывать несуществующие размеры сторон
# Площадь по формуле Герона: 
# S = √(p * (p - a) * (p - b) * (p - c)),
# где a, b и c - длины сторон треугольника;
# p - полупериметр треугольника: p = (a + b + c) / 2.)
# и периметр - свойства треугольника

import math

class Triangle:
    def __init__(self, a, b, c):
        self.__a = a
        self.__b = b
        self.__c = c 

    @property
    def a(self):
        return self.__a

    @a.setter
    def a(self, value):
        if value <= 0:
            return ValueError("Сторона должна быть положительным числом.")
        if value + self.b > self.c and value + self.c > self.b:
            self.__a = value
        else:
            return ValueError("Не существует треугольника с такими сторонами.")

    @property
    def b(self):
        return self.__b

    @b.setter
    def b(self, value):
        if value <= 0:
            return ValueError("Сторона должна быть положительным числом.")
        if value + self.a > self.c and value + self.c > self.a:
            self.__b = value
        else:
            return ValueError("Не существует треугольника с такими сторонами.")

    @property
    def c(self):
        return self.__c

    @c.setter
    def c(self, value):
        if value <= 0:
            return ValueError("Сторона должна быть положительным числом.")
        if value + self.a > self.b and value + self.b > self.a:
            self.__c = value
        else:
            return ValueError("Не существует треугольника с такими сторонами.")

    @property
    def perimeter(self):
        return self.a + self.b + self.c

    @property
    def area(self):
        p = self.perimeter / 2  # Полупериметр
        return math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))

    def __str__(self):
        return (f"Треугольник со сторонами: a={self.a}, b={self.b}, c={self.c}, "
                f"Периметр: {self.perimeter}, Площадь: {self.area:.2f}")

# # Существующий треугольник
# try:
#     triangle1 = Triangle(3, 4, 5)
#     print(triangle1)
# except ValueError as error:
#     print("Ошибка:", error)

# # Несуществующий треугольник
# try:
#     triangle2 = Triangle(1, 2, 3)  
# except ValueError as error:
#     print("Ошибка:", error)

# # Пример некорректной стороны (отрицательное значение)
# try:
#     triangle3 = Triangle(-1, 2, 3)  
# except ValueError as error:
#     print("Ошибка:", error)

# # Пример некорректной стороны (ноль)
# try:
#     triangle4 = Triangle(0, 2, 3)  
# except ValueError as error:
#     print("Ошибка:", error)

# Функция для создания треугольника
def create_triangle(a, b, c):
    try:
        triangle = Triangle(a, b, c)
        print(triangle)
    except ValueError as error:
        print("Ошибка:", error)

create_triangle(3, 4, 5)   # Существующий треугольник
create_triangle(1, 2, 3)   # Несуществующий треугольник
create_triangle(-1, 2, 3)  # Некорректная сторона (отрицательное значение)
create_triangle(0, 2, 3)   # Некорректная сторона (ноль)