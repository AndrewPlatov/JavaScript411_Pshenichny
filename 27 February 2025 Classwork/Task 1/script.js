const correctAnswer = generateQuestion();
let timeLeft = 30;
let timer;

document.getElementById('check-button').addEventListener('click', checkAnswer);

// Создаем два случайных числа. Ограничимся от 0 до 9. После чего найдем их сумму.
function generateQuestion() {
    const num1 = Math.round(Math.random() * 10);   
    const num2 = Math.round(Math.random() * 10);
    document.getElementById('question-container').textContent = `${num1} + ${num2}`;
    return num1 + num2;
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
}

startTimer();