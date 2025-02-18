document.getElementById('changeColor').addEventListener('click', function() {
    
    let red = document.getElementById('red').value;
    let green = document.getElementById('green').value;
    let blue = document.getElementById('blue').value;

    // Не уверен, что это корректно, однако работает. Вычитал, что предельное значение для цветов 255. 
    // Насколько я помню, оператор && выполняет функцию логического И. Используется только с типом boolean, 
    // т.е. true или false. TRUE выводится только тогда, когда все операнды (условно переменные) тоже равны true. 
    // Если есть хоть один false, то все выражение будет false.

    if (isColor(red) && isColor(green) && isColor(blue)) {
        document.body.style.backgroundColor = `rgb(${red}, ${green}, ${blue})`;
    } else {
        alert('Пожалуйста, введите значения от 0 до 255.');  // Хоть Вы и не любите alert, но не знаю как иначе ))
    }
});

function isColor(value) {
    return value >= 0 && value <= 255;
}

// И из чисто теоретического интереса: возможно ли применение той функции случайного числа?
// Например, если я хочу чтобы три числа выпадали на рандоме.