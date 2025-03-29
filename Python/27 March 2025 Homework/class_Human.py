class HumanInfo:
    def __init__(self, name, lastname, height = "", age = "", year = None, nationality = None):
        self.name = name
        self.lastname = lastname
        self.height = height
        self.age = age
        self.year = year
        self.nationality = nationality

    def __str__(self):
        return (f"Человек:\n"
                f"Имя: {self.name}\n"
                f"Фамилия: {self.lastname}\n"
                f"Рост: {self.height}\n"
                f"Возраст: {self.age}\n"
                f"Год рождения: {self.year}\n"
                f"Национальность: {self.nationality}")

human1 = HumanInfo(name = "Andrew", lastname = "Pshenichny", height = 171, age = 26, year = 1998, nationality = "Russian")
print(human1)
print()

human2 = HumanInfo("Alex", "Alexandrov")
print(human2)
print()

human3 = HumanInfo("Elena", "Antonova", 168, 48, 1977)
print(human3)