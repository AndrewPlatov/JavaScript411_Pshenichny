// Для начала создадим функцию. Будем использовать var, а не let, так как с помощью
// var сможем переопределять значения и сможем вносить данные в таблицу несколько раз.
document.getElementById('submitButton').addEventListener('click', function() {
    var name = document.getElementById('name').value;
    var email = document.getElementById('email').value;
    var message = document.getElementById('message').value;

    // Создаем строку таблицы, к которой будем далее крепить ячейки 
    var newRow = document.createElement('tr');

    // Теперь создаем ячейки для данных, которые введет наш пользователь
    var nameCell = document.createElement('td');
    nameCell.textContent = name;        // ячейка с именем

    var emailCell = document.createElement('td');
    emailCell.textContent = email;      // ячейка с имейл

    var messageCell = document.createElement('td');
    messageCell.textContent = message;  // ячейка с каким-то текстом от пользователя

    // А теперь довавляем (крепим) ячейки в созданную строку
    newRow.appendChild(nameCell);
    newRow.appendChild(emailCell);
    newRow.appendChild(messageCell);

    // Теперь строку с данным крепим к таблице
    document.getElementById('tableBody').appendChild(newRow);

    // Очищаем поля формы, чтобы можно было ввести новые данные
    document.getElementById('subscriptionForm').reset();

    // Удаляем класс hidden у таблицы, так как изначально я ее скрыл с помощью стилей, 
    // чтобы не было вероятности ее появления при прогрузке страницы (а она прогрузилась во всех случаях).
    // Таким образом, после удаления класса она волшебным образом появится.
    document.getElementById('resultTable').classList.remove('hidden');
});