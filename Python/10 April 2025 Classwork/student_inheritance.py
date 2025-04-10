# Унаследовать класс Человек, создав класс "студент". У студента есть массив оценок, номер группы и курс.
# Напечатать студента: 
# Вася, группа 1234, Питон, [12, 10, 6, 10, 8, 12, 10]

class Human:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name


class Student(Human):
    def __init__(self, name, group_number, course, grades):
        self.name = name
        self.group_number = group_number
        self.course = course
        self.grades = grades

    def __str__(self):
        return f"{self.name}, группа {self.group_number}, курс {self.course}, оценки {self.grades}"


student = Student("Вася", "1234", "Питон", [12, 10, 6, 10, 8, 12, 10])
print(student)