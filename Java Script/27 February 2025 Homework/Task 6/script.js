// На страничке есть поле ввода и кнопка. При нажатии на кнопку
// в консоль выводится сообщение: "Аааа, это цикл!" столько раз,
// какое число в поле ввода.

document.getElementById('loopButton').addEventListener('click', function() {
    const count = document.getElementById('inputField').valueAsNumber;
    for (let i = 0; i < count; i++) {
        console.log('Аааа, это цикл!');
    }
    console.log('Наконец-то это все!');
});