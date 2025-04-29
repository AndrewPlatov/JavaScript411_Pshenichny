def get_raw_data():
    import psycopg

    # Подключиться к БД
    conn = psycopg.connect(
        dbname='students',
        user='andrewpshenichny',
    )
    cursor = conn.cursor()

    # Прочитать
    cursor.execute('SELECT first_name, row_number, comp FROM group411 WHERE NOT comp IS NULL')
    data = cursor.fetchall()

    # Отключиться
    cursor.close()
    conn.close()
    return data

def understand(data):
    # Определяем количество парт и мест
    num_rows = 4  # Количество парт
    num_comps = 4  # Количество мест за партой
    
    # Инициализируем массив студентов
    students = [[None for _ in range(num_comps)] for _ in range(num_rows)]
    
    max_name_length = 0  # Переменная для хранения максимальной длины имени
    
    for s in data:
        name, row, comp = s
        students[row - 1][comp - 1] = name
        
        # Обновляем максимальную длину имени
        max_name_length = max(max_name_length, len(name))

    return students, max_name_length

def draw(classroom, max_name):
    line = '+' + 4 * ('-' * max_name + '+')
    print(line)
    
    for row in classroom:
        row_str = '|'
        for chair in row:
            if chair:
                row_str += ('%%%is' % max_name) % chair + '|'
            else:
                row_str += ' ' * max_name + '|'
        print(row_str)
        print(line)

def update(name, row, comp):
    import psycopg

    # Подключиться к БД
    conn = psycopg.connect(
        dbname='students',
        user='andrewpshenichny',
    )
    
    cursor = conn.cursor()

    # Записать и подтвердить
    cursor.execute("UPDATE group411 SET row_number=%s, comp=%s WHERE first_name=%s", (row, comp, name))
    
    conn.commit()  # Подтвердить изменения

    # Отключиться
    cursor.close()
    conn.close()



update('Андрей', 1, 2)
draw(*understand(get_raw_data()))