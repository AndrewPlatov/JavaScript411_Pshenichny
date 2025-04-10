# Унаследовать класс Человек, создав класс "студент". У студента есть массив оценок, номер группы и курс.
# Напечатать студента: 
# Вася, группа 1234, Питон, [12, 10, 6, 10, 8, 12, 10]

class Human:
    def __init__(self, name):
        self.__name = name  

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value


class Student(Human):
    def __init__(self, name, group_number, course, grades):
        self._Human__name = name
        self.__group_number = group_number
        self.__course = course
        self.__grades = grades

    @property
    def group_number(self):
        return self.__group_number

    @group_number.setter
    def group_number(self, value):
        self.__group_number = value

    @property
    def course(self):
        return self.__course

    @course.setter
    def course(self, value):
        self.__course = value

    @property
    def grades(self):
        return self.__grades

    @grades.setter
    def grades(self, value):
        self.__grades = value  

    def __str__(self):
        return f"{self.name}, группа {self.group_number}, курс {self.course}, оценки {self.grades}"


student = Student("Вася", "1234", "Питон", [12, 10, 6, 10, 8, 12, 10])
print(student)
