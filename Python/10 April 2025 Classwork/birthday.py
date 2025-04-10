from datetime import datetime

class Human:

    #               0     1         2
    def __init__(self, name, birthday):  # Метод - фунцкия в классе
        self.name = name                 # Поле - переменная в классе
        self.birthday = birthday


h = Human('Wera', datetime(1986, 8, 6))
print('Дата рождения', h.birthday)
h.age = 18
print('Возраст', h.age)
h.birthday = 'Большой секрет'
print('День рождения', h.birthday) 