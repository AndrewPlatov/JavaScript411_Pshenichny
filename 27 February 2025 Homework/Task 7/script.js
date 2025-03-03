// На страничке изначально пусто, а при загрузке всплывает сообщение:
// "введите число". Появляется столько заголовков h1 с надписью
// "Это тоже цикл и гадский промпт на входе!", сколько ввели

// Запрашиваем у пользователя число
const userInput = prompt("Введите число");
const count = Number(userInput);

// Создаем количество заголовков h1 в зависимости от введенного числа
const outputDiv = document.getElementById('output');
for (let i = 0; i < count; i++) {
    const h1 = document.createElement('h1');
    h1.textContent = "Это тоже цикл и гадский промпт на входе!";
    outputDiv.appendChild(h1);
}

// Обработчик события для кнопки берем из предыдущей задачи
document.getElementById('loopButton').addEventListener('click', function() {
    const count = document.getElementById('inputField').valueAsNumber;
    for (let i = 0; i < count; i++) {
        console.log('Аааа, это цикл!');
    }
    console.log('Наконец-то!');
});