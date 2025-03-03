// На страничке изначально пусто, но создается таблица джаваскриптом, содержащая
// квадраты целых чисел от 1 до 10.

// Используем селектор '#squaresTable tbody' для указания конкретного элемента чтобы с ним взаимодействовать.
const tableBody = document.querySelector('#squaresTable tbody');

// Заполняем таблицу квадратами чисел от 1 до 10. Для этого необходимо сначала создать строку.
// Затем создать ячейку для числа и отдельную ячейку для его квадрата.
for (let i = 1; i <= 10; i++) {
    const row = document.createElement('tr'); 
    const numberCell = document.createElement('td'); 
    const squareCell = document.createElement('td'); 

    // Затем заполняем ячейку числом, а следом другую ячейку с квадратом числа.
    numberCell.textContent = i;
    squareCell.textContent = i * i; 
 
    row.appendChild(numberCell); 
    row.appendChild(squareCell); 
    tableBody.appendChild(row); 
}