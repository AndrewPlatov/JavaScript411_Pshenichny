import math

class Triangle:
    def __init__(self, a, b, c):
        self.__a = None
        self.__b = None
        self.__c = None
        self.a = a  # Используем сеттер для проверки
        self.b = b  
        self.c = c  

    @property
    def a(self):
        return self.__a

    @a.setter
    def a(self, value):
        if value <= 0:
            raise ValueError("Сторона должна быть положительным числом.")
        if self.__b is not None and self.__c is not None:
            if value + self.__b < self.__c or value + self.__c < self.__b:
                raise ValueError("Не существует треугольника с такими сторонами.")
        self.__a = value

    @property
    def b(self):
        return self.__b

    @b.setter
    def b(self, value):
        if value <= 0:
            raise ValueError("Сторона должна быть положительным числом.")
        if self.__a is not None and self.__c is not None:
            if value + self.__a < self.__c or value + self.__c < self.__a:
                raise ValueError("Не существует треугольника с такими сторонами.")
        self.__b = value

    @property
    def c(self):
        return self.__c

    @c.setter
    def c(self, value):
        if value <= 0:
            raise ValueError("Сторона должна быть положительным числом.")
        if self.__a is not None and self.__b is not None:
            if value + self.__a < self.__b or value + self.__b < self.__a:
                raise ValueError("Не существует треугольника с такими сторонами.")
        self.__c = value

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