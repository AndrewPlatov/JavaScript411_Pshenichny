# Task 4
# Класс Книга: Название, автор, год издания, содержание книги (пример! не надо всю копировать! Можно "Репку" в качестве примера...) 

# Для начала создадим свой класс (название, автор, год издания, краткое содержание, собственное мнение)
class Book:
    def __init__(self, name, author, year, briefly, opinion = ""):
        self.name = name
        self.author = author
        self.year = year
        self.briefly = briefly
        self.opinion = opinion

    # Далее напишем функцию для вывода информации использую f-строку
    def display_info(self):
        print(f"Название: {self.name}")
        print(f"Автор: {self.author}")
        print(f"Год издания: {self.year}")
        print(f"Краткое содержание: {self.briefly}")
        print(f"Мнение: {self.opinion}")
        print()

# Теперь создадим три класса Book. Очень важно соблюдать порядок (название, автор, год, описание, мнение).
# Но если один из пунктов не указан (пропущен), то работать не будет, проверено =)
book1 = Book("1984", "Джордж Оруэлл", 1949, "Дистопия о тоталитарном обществе.", "Как лечить алкоголизм курением")
book2 = Book("Война и мир", "Лев Толстой", 1869, "Эпопея о жизни русского общества во время Наполеоновских войн.")
book3 = Book("Квантовая механика", "Альберт Месси", 1958, "Основы квантовой механики и её применение в физике.", "Я понял, что я ничего не понял")

# Выводим информацию
print("Информация о книгах:")
book1.display_info()
book2.display_info()
book3.display_info()

# Таким образом, в программе реализована возможность присваивать и выводить информацию, не прописывая в ручную,
# как я это сделал в первых заданиях. И теперь мне понятно практическое применение классов: уменьшение обьема кода
# и практичность. 