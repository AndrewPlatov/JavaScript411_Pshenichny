function main_func() { 
    console.log('Страница готова к работе'); 
    add_table_to_page(create_table());
} 

function add_table_to_page(tbl) {
    // Функция добавляет кем-то созданную таблицу в тело страницы
    document.body.appendChild(tbl);
    // прикрепляем элемент к телу страницы
}

function create_table(columns, rows) {
    let result = document.createElement('table');

    let tr = document.createElement('tr');
    result.appendChild(tr);

    let td = document.createElement('td');
    tr.appendChild(td);

    td.textContent = 'mew';
    
    return result;
}

window.addEventListener( 
    'load', 
    main_func 
);