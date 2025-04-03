# Сделайте проверку, чтобы вводимое было не только числом, но и могло быть разумным для длины комнаты в метрах

class Room:
    
    def __init__(self, w, l, h=2.5):
        self.__width = w
        self.__length = l
        self.__height = h

    def set_length(self, new_length):
        # Сеттер позволяет дополнительно контролировать вводимые данные
        if isinstance(new_length, float) or isinstance(new_length, int) and new_length > 0 and new_length <= 50:
            self.__length = new_length
        else:
            print("ДЛИНА ДОЛЖНА БЫТЬ ПОЛОЖИТЕЛЬНЫМ ЧИСЛОМ И НЕ БОЛЬШЕ 50 МЕТРОВ. ВВЕДЕНО: %s" % (new_length)) 

    def area(self):
        return self.__width * self.__length
    
    def __str__(self):
        return f'Комната имеет размеры: длина = {self.__length}, ширина = {self.__width}'
    
r = Room(3, 6)
print(r)
print('Площадь комнаты: ', r.area())
r.set_length(100)
print(r)
print('Площадь комнаты: ', r.area())
r.set_length("Очень длинная")