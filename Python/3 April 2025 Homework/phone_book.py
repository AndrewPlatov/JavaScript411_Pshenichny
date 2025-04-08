# Класс "телефонная книга". 
# Храните данные, как хотите, но просто по текстовому вводу класс должен искать частичные совпадения (без опечаток).
# т.е. если ему вводишь "вер" он должен найти: вера, вероника, витя@север.ру.
# это будет геттер. Он возвращает список вариантов, с емейлами и телефонами.

class PhoneBook:
    def __init__(self):
        # Инициализируем телефонную книгу как пустой словарь
        self.contacts = {}

    def add_contact(self, name, phone, email):
        # Добавляем контакт в телефонную книгу
        self.contacts[name] = (phone, email)

    def search(self, query):
        # Ищем по частичному совпадению
        results = []
        for name, (phone, email) in self.contacts.items():
            if query.lower() in name.lower():     # Поиск по имени
                results.append((name, phone, email))
            elif query.lower() in phone:          # Поиск по телефону
                results.append((name, phone, email))
            elif query.lower() in email.lower():  # Поиск по email
                results.append((name, phone, email))
        return results

phone_book = PhoneBook()
    
# Добавляем контакты
phone_book.add_contact("Вера", "+7 123 456-78-90", "vera@example.com")
phone_book.add_contact("Вероника", "+7 987 654-32-10", "veronika@example.com")
phone_book.add_contact("Витя", "+7 555 555-55-55", "vitya@sever.ru")
phone_book.add_contact("Валера", "+7 800 555-35-35", "valera@norm.com")
    
# Выполняем поиск
search_query = input("Введите запрос для поиска: ")
results = phone_book.search(search_query)
    
# Выводим результаты поиска
if results:
    print("Найденные контакты:")
    for name, phone, email in results:
        print(f"Имя: {name}, Телефон: {phone}, Email: {email}")
else:
    print("Контакт не найден.")