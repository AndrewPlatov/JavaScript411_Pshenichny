let currentQuestionIndex = 0; // Добавляем индекс вопроса, чтобы он менялся в зависимости от числа задач
let correctAnswer;
let timeLeft = 30;
let timer;
const operations = ['+', '-', '*', '/']; // Перечисляем арифметические операции, которые задействуем в цикле

document.getElementById('check-button').addEventListener('click', checkAnswer);

// Создаем два случайных числа. Ограничимся от 0 до 9. После чего найдем их сумму.
function generateQuestion() {
    const operation = operations[currentQuestionIndex]; // происходит выбор текущей математической операции, которая будет использоваться для генерации вопроса
    const num1 = Math.round(Math.random() * 10);   
    const num2 = Math.round(Math.random() * 10);
    document.getElementById('question-container').textContent = `${num1} ${operation} ${num2}`; // добавил ${operation} чтобы менялись не только числа, но и знак
    
// Цикл для определения правильного ответа в зависимости от операции
    if (operation === '+') {
        correctAnswer = num1 + num2;
    } else if (operation === '-') {
        correctAnswer = num1 - num2;
    } else if (operation === '*') {
        correctAnswer = num1 * num2;
    } else if (operation === '/') {
        correctAnswer = num1 / num2;
    }
}

// С таймером вычитал на stackoverflow
function startTimer() {
    timer = setInterval(() => {
        timeLeft--; // timeLeft-- уменьшает наше остаточное время на 1 секунду

        // Если время вышло, останавливаем таймер и проверяем ответ
        if (timeLeft < 0) {
            clearInterval(timer);  // clearInterval останавливает наш таймер, так как он больше не нужен
            checkAnswer();         // ОЧЕНЬ ВАЖНОЕ НО !!! ДАННАЯ СТРОКА ПОЗВОЛЯЕТ НАМ ПРОВЕРИТЬ ВВЕДЕНЫЙ ОТВЕТ ДАЖЕ ЕСЛИ ПОЛЬЗОВАТЕЛЬ 
                                   // НЕ НАЖАЛ НА КНОПКУ И НЕ ПРОИЗОШЛО СОБЫТИЕ НАЖАТИЯ !!! ОДНАКО ЕСЛИ УБРАТЬ ДАННУЮ СТРОКУ, ТО ВООБЩЕ 
                                   // НИЧЕГО НЕ ПРОИЗОЙДЕТ. ВРЕМЯ ОСТАНОВИТСЯ И НЕ БУДЕТ НИКАКИХ СООБЩЕНИЙ !!!
        }

        // Это нужно для того, чтобы наше время обновлялось. 1000 = 1 секунда, что является нашим шагом отсчета.
        // Также нужно ограничение в виде Math.max(timeLeft, 0), так как указанный ноль не дает отсчету сваливаться в отрицательное значние.
        // Ну а timeLeft был задан нами в самом начале. Таким образом создаем диапазон для таймера.
        document.getElementById('time-left').textContent = Math.max(timeLeft, 0);
    }, 1000);
}

// Далее проверяем наш ответ, а точнее соответствие введенных данных пользователя с вычислением.
// Для начала останавливаем таймер, если время не успело выйти. Далее проверяем введенное значение со значением посчитанным. 
// Ну а вишенка на торте - вывод сообщения о правильности ответа или неправильности. И вывод правильного ответа, если введено неверно.
function checkAnswer() {
    clearInterval(timer);
    const userAnswer = Number(document.getElementById('user-answer').value);
    const resultDiv = document.getElementById('result');
    resultDiv.textContent = userAnswer === correctAnswer ? "Правильно!" : `Неправильно! Правильный ответ: ${correctAnswer}`;

// Создаем переход к следующему вопросу, сбрасывая предыдущий пример и перезапуская генерацию
    currentQuestionIndex++;
    if (currentQuestionIndex < operations.length) {
        resetGame();
        generateQuestion();
    } else {
        resultDiv.textContent += " Вы закончили!"; // Завершение всех задач и отключение кнопки, если все индексы задач закончились
        document.getElementById('check-button').disabled = true;
    }
}

function resetGame() {
    timeLeft = 30;
    document.getElementById('user-answer').value = ''; // Сбрасываем поле ввода и сбрасываем все сообщения, выведенные ранее
    document.getElementById('result').textContent = ''; 
    startTimer();
}

// Запускаем генератор задач и таймер
generateQuestion();
startTimer();