import psycopg

# Подключаемся к базе данных. Задействуем исключения чтобы выводить сообщения об ошибке подключения к БД

try:
    conn = psycopg.connect(
        dbname='students',
        user='andrewpshenichny'
    )
    
    cursor = conn.cursor()
    
    # Получаем данные о складах
    cursor.execute('SELECT id, city, toponim, building, office FROM warehouse')
    warehouses = cursor.fetchall()
    
    print("Склады:")
    for index, warehouse in enumerate(warehouses):
        print(f"{index + 1}. ID: {warehouse[0]}, Город: {warehouse[1]}, Топоним: {warehouse[2]}, Здание: {warehouse[3]}, Офис: {warehouse[4]}")

    # Запрашиваем у пользователя номер нужного склада
    wh_choice = int(input('Введите номер нужного склада: ')) - 1

    # Проверяем корректность выбора
    if 0 <= wh_choice < len(warehouses):
        selected_warehouse_id = warehouses[wh_choice][0] 

        # Получаем товары для выбранного склада с полями name, price и quantity
        cursor.execute('SELECT name AS "Название товара", price AS "Цена", quantity AS "Количество" FROM good_unit WHERE wh = %s', (selected_warehouse_id,))
        goods = cursor.fetchall()
        
        print("Товары на складе:")
        for good in goods:
            print(f" - {good[0]}: Цена - {good[1]}, Количество - {good[2]}")

        # Получаем цены и количество товаров для расчета общей стоимости
        cursor.execute('SELECT price, quantity FROM good_unit WHERE wh = %s', (selected_warehouse_id,))
        prices_and_quantities = cursor.fetchall()

        total_price = sum(price * quantity for price, quantity in prices_and_quantities)  # Суммируем стоимость товаров
        print(f"Общая стоимость товаров на складе: {total_price}")
    else:
        print("Некорректный номер склада.")
        
except Exception as e:
    print(f"Произошла ошибка: {e}")
