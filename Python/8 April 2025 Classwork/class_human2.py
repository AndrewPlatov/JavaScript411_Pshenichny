from datetime import datetime

class Human:
    def __init__(self, name, born_date):
        self._name = name 
        self._born_date = born_date

    @property
    def name(self):
        return self._name

    @property
    def born_date(self):
        return self._born_date

    @property
    def age(self):
        today = datetime.now()
        age = today.year - self._born_date.year - ((today.month, today.day) < (self._born_date.month, self._born_date.day))
        return age

born_date = datetime(1998, 6, 2)  
human2 = Human("Andrew", born_date)
print(human2.name) 
print(human2.age)