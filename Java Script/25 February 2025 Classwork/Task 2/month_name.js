// Задача: Вывести на страницу HTML таблицу
// с 4-мы сезонами года.
// V Для каждого месяца указать русское название
// Фон покрасить средствами JS+CSS

function create_season_table() {
    // Вывести на страницу HTML таблицу
    // Элемент создается с названием в текстовом виде
    // надо созданный объект сохранить в переменную или константу
    const tbl = document.createElement('table');
    // Создать элемент
    // Прикрепить элемент к телу страницы
    document.body.appendChild(tbl);
    const tr = document.createElement('tr');
    document.body.appendChild(tr);

    // Создали строку таблицы (tr) 
    let tr = document.createElement('tr');
    // Ссылка на таблицу уже была, мы к таблице прикрепили строку
    tbl.appendChild(tr);
    
    // Создали переменную и первую ячейку
    let td = document.createElement('td');
    tr.appendChild(td);
    td.textContent = "Весна";

    // переменная уже есть, создали вторую ячейку
    td = document.createElement('td');
    tr.appendChild(td);
    td.textContent = "Лето";

    tr = document.createElement('tr');
    // Ссылка на таблицу уже была, мы к таблице прикрепили строку
    tbl.appendChild(tr);
    // Создали переменную и первую ячейку
    td = document.createElement('td');
    tr.appendChild(td);
    td.textContent = "Осень";

    // переменная уже есть, создали вторую ячейку
    td = document.createElement('td');
    tr.appendChild(td);
    td.textContent = "Зима";
    /*
    <table>  // уже есть
        <tr>
        <tr>  // уже есть
            <td>Весна</td>
            <td>Лето</td>
        </tr>
        <tr>
            <td>Осень</td>
            <td>Зима</td>
        </tr>
     </table>
    */
}

window.addEventListener(
    'load',  // Сделай так, браузер, чтобы после загрузки страницы
    create_season_table  // вызывалась эта функция 
);


function getWrittenMonth(){
    // Для каждого месяца указать русское название
    const date = new Date();  // Текущая дата и время
    console.log(date);
    // date.getMonth() в JS возвращает месяцы С НУЛЯ
    const all_names = [  // Квадратные скобки - литерал списка
        'января',   // 0
        'февраля',  // 1
        'марта',    // 2
        'апреля',   // 3
        'мая',      // 4
        'июня',     // 5
        'июля',     // 6
        'августа',  // 
        'сентября',
        'октября',
        'ноября',
        'декабря'
    ];
    // return all_names[4];  // Вернули май
    const month_number = date.getMonth();
    return all_names[month_number];
}