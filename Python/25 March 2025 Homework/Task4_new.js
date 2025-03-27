let books = [
    ["1984", "Джордж Оруэлл", 1949, "Дистопия о тоталитарном обществе.", "Как лечить алкоголизм курением"],
    ["Война и мир", "Лев Толстой", 1869, "Эпопея о жизни русского общества во время Наполеоновских войн.", "Очень долго, но невероятно захватывает"],
    ["Квантовая механика", "Альберт Месси", 1958, "Основы квантовой механики и её применение в физике.", "Я понял, что я ничего не понял"]
];

function create_table() {
    // Создание элемента таблицы
    let tbl = document.createElement('table'); 
    
    // Создание заголовка таблицы
    let header = document.createElement('tr');
    let headers = ['Название', 'Автор', 'Год', 'Описание', 'Отзыв'];
    for (let h of headers) {
        let th = document.createElement('th');
        th.textContent = h;
        header.appendChild(th);
    }
    tbl.appendChild(header);
    
    // Добавление строк с книгами
    for (let b of books) {
        let table_row = book(...b);
        tbl.appendChild(table_row);
    }

    // Прикрепление таблицы к документу
    document.body.appendChild(tbl);
}

// Функция для создания строки таблицы
function book() {
    let row = document.createElement('tr');
    let td;
    for (let elmi of arguments) {
        td = document.createElement('td');
        td.textContent = elmi;
        row.appendChild(td);
    }
    return row;
}

// Вызов функции для создания таблицы
create_table();