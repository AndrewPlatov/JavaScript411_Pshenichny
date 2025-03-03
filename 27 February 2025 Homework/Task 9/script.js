// На страничке есть две кнопки "все появить" и "все спрятать" и таблица.
// Таблица должна появляться и исчезать по нажатии на кнопку.

const showButton = document.getElementById('showButton');
const hideButton = document.getElementById('hideButton');
const table = document.getElementById('squaresTable');

// Делаем таблицу видимой 
showButton.addEventListener('click', function() {
    table.style.display = 'table';
});

// Прячем таблицу
hideButton.addEventListener('click', function() {
    table.style.display = 'none';
});