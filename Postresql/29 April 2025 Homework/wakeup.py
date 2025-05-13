import psycopg

# Подключение к базе данных с обработкой ошибок
try:
    with psycopg.connect(
        dbname='students',
        user='andrewpshenichny'
    ) as conn:
        with conn.cursor() as cursor:
            # Получение общего времени без учета сна
            cursor.execute('''
                SELECT COALESCE(SUM(EXTRACT(EPOCH FROM (end_time - start_time))), 0) AS total_seconds
                FROM activities;
            ''')
            total_seconds = cursor.fetchone()[0]
            
            # Получение суммы времени по категориям
            cursor.execute('''
                SELECT c.name, COALESCE(SUM(EXTRACT(EPOCH FROM (a.end_time - a.start_time))), 0) AS category_seconds
                FROM activities a
                JOIN categories c ON a.category_id = c.id
                GROUP BY c.name;
            ''')
            category_times = cursor.fetchall()
            
            # Вывод общего времени и по категориям с процентами
            print(f"Общее время: {total_seconds/3600:.2f} часов")
            for category_name, seconds in category_times:
                hours = seconds / 3600
                percent = (seconds / total_seconds) * 100 if total_seconds else 0
                print(f"{category_name}: {hours:.2f} часов ({percent:.2f}%)")
except psycopg.Error as e:
    print(f"Ошибка при подключении или выполнении запроса: {e}")