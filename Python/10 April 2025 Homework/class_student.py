# Дописать класс студент. У него должны быть необходимые свойства, геттеры и сеттеры. Например, свойство "средний балл"
# Заметьте, что студент наследует свойство "возраст", которое публично и успешно может быть использовано
# Добавьте магические метода str и напечатайте человека с возрастом (Вася, 25), а студента - с именем, возрастом , курсом, группой и средним баллом

from datetime import datetime

class Human:
    def __init__(self, name, birthday):
        self.__name = name
        self.__birthday = birthday

    @property
    def name(self):
        return self.__name

    @property
    def age(self):
        today = datetime.now()
        age = today.year - self.__birthday.year - ((today.month, today.day) < (self.__birthday.month, self.__birthday.day))
        return age

    @name.setter
    def name(self, value):
        self.__name = value


class Student(Human):
    def __init__(self, name, birthday, group, course):
        super().__init__(name, birthday)
        self.__marks = []
        self.__group = group
        self.__course = course

    @property
    def marks(self):
        return self.__marks

    @marks.setter
    def marks(self, new_mark):
        if isinstance(new_mark, int) and 0 < new_mark < 13:
            self.__marks.append(new_mark)

    @property
    def average_grade(self):
        if not self.__marks:
            return 0
        return sum(self.__marks) / len(self.__marks)

    @property
    def group(self):
        return self.__group

    @property
    def course(self):
        return self.__course

    def __str__(self):
        return f"{self.name}, возраст {self.age}, группа {self.group}, курс {self.course}, средний балл {self.average_grade:.2f}"


s = Student("Вася", datetime(2000, 1, 1), '411', 'Python')
s.marks = 12
s.marks = 10
s.marks = 6
s.marks = 10
s.marks = 8

print(s) 
print(f"Оценки: {s.marks}")
print(f"Возраст: {s.age}")