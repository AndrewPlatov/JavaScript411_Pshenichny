// Для начала создадим функцию
document.getElementById("subscribeButton").addEventListener("click", function() {
    // Получаем значения из формы
    const name = document.getElementById("name").value;
    const email = document.getElementById("email").value;
    const comment = document.getElementById("comment").value;

    // Скрываем форму
    document.getElementById("subscriptionForm").style.display = "none";

    // Отображаем таблицу
    const tableBody = document.getElementById("tableBody");
    const resultTable = document.getElementById("resultTable");

    // Добавляем строки в таблицу
    const fields = [
        { label: 'Имя', value: name },
        { label: 'Email', value: email },
        { label: 'Комментарий', value: comment }
    ];

    // Прикрепляем ячейки
    fields.forEach(field => {
        const row = document.createElement('tr');
        const cell1 = document.createElement('td');
        const cell2 = document.createElement('td');

        cell1.textContent = field.label;
        cell2.textContent = field.value;

        row.appendChild(cell1);
        row.appendChild(cell2);
        tableBody.appendChild(row);
    });

    // Выводим итоговую таблицу
    resultTable.style.display = "table";
});