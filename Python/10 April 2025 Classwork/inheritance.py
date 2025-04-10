class Car:
    
    def  __init__(self, wheels=4):
        self.__wheels = 4
        self.__hours = 0
        self._x = 0   # Поле "условно защищённое" - вы можете пользоваться им как публичным

    def move(self, speed=60):
        self.__hours += 1
        self._x += speed

    def __str__(self):
        return "Машина уехала на " + str(self._x) + " километров за " + str(self.__hours) + " часов."

mercedes = Car()
print(mercedes._x)  # РЕАЛЬНО ОНО ПУБЛИЧНОЕ!
# не надо так делать...
mercedes.move()
mercedes.move()
mercedes.move()
mercedes.move()
mercedes.move()
mercedes.move()
print(mercedes)


class Truck(Car):

    # __init__ унаследован!
    # move унаследован!

    def __str__(self):
        return "Грузовик уехал на " + str(self._x) + " километров и молодец"

man = Truck(8)
man.move(20)
man.move(50)
man.move(70)
man.move(10)
man.move(45)
print(man)