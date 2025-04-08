class Human:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

human1 = Human("Иван")
print(human1.name)