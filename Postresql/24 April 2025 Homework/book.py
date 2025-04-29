import psycopg

def read_books_from_file(file_path):
    books = []
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            title, author, year = line.strip().split(';')
            books.append((title, author, int(year)))  # Преобразуем год в целое число
    return books

def insert_books_to_db(books):
    # Подключиться к БД
    conn = psycopg.connect(
        dbname='your_database_name',
        user='your_username'
    )
    
    cursor = conn.cursor()

    # Вставка книг в таблицу
    for title, author, year in books:
        cursor.execute(
            "INSERT INTO books (title, author, year) VALUES (%s, %s, %s)",
            (title, author, year)
        )

    conn.commit()  # Подтвердить изменения

    # Отключиться
    cursor.close()
    conn.close()

    file_path = 'books.txt'
    
    # Чтение книг из файла
    books = read_books_from_file(file_path)
    
    # Вставка книг в БД
    insert_books_to_db(books)

    print("Книги успешно добавлены в базу данных.")