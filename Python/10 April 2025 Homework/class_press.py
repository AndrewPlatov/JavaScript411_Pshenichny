# Создайте класс Печатное Издание. У него есть название и год издания. Унаследуйте печатное издание, создав классы.
# Книга, Журнал. У книги есть автор, у журнала есть издательство, номер и периодичность выхода.
# Создайте массив за 5 лет ежемесячных журналов "Работница" c 2015 года. Создайте массив из 3 разных книг.
# Запишите массивы в файл, создайте функции записи в файл
# 1. Печатного издания, книги, журнала, используя super()

class Press:
    def __init__(self, name, publication_year):
        self.name = name
        self.publication_year = publication_year

    def to_string(self):
        return f"{self.name}, {self.publication_year}"

class Book(Press):
    def __init__(self, name, publication_year, author):
        super().__init__(name, publication_year)
        self.author = author

    def to_string(self):
        return f"Книга: {super().to_string()}, Автор: {self.author}"

class Magazine(Press):
    def __init__(self, name, publication_year, publisher, issue_number, frequency):
        super().__init__(name, publication_year)
        self.publisher = publisher
        self.issue_number = issue_number
        self.frequency = frequency

    def to_string(self):
        return f"Журнал: {super().to_string()}, Издатель: {self.publisher}, Номер издания: {self.issue_number}, Периодичность: {self.frequency}"

def create_magazines():
    magazines = []
    for year in range(2015, 2020):  # с 2015 по 2019
        for month in range(1, 13):  # 12 месяцев
            magazine = Magazine(
                name="Работница",
                publication_year=year,
                publisher="Издательство Работница",
                issue_number=month,
                frequency="Ежемесячно"
            )
            magazines.append(magazine)
    return magazines

def create_books():
    books = [
        Book("Книга 1", 2018, "Автор 1"),
        Book("Книга 2", 2019, "Автор 2"),
        Book("Книга 3", 2020, "Автор 3")
    ]
    return books

def write_to_file(magazines, books, filename):
    with open(filename, 'w', encoding='utf-8') as file:
        for magazine in magazines:
            file.write(magazine.to_string() + '\n')
        
        for book in books:
            file.write(book.to_string() + '\n')

magazines = create_magazines()
books = create_books()

filename = "printed_publications.txt"
write_to_file(magazines, books, filename)

print(f"Данные успешно записаны в файл {filename}.")