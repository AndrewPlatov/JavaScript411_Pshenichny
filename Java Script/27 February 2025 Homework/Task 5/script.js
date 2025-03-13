// Напишите страничку и два поля ввода типа number
// Чтобы получить значение нужно использовать 
// valueAsNumber вместо обычного number
// Выведите в консоль сумму, разность и произведение введенных чисел.
// Отчетность: страничка html, файл js из 5-10 строк.

document.getElementById('calculateButton').addEventListener('click', function() {
    const num1 = document.getElementById('number1').valueAsNumber;
    const num2 = document.getElementById('number2').valueAsNumber;
    console.log('Сумма = ', num1 + num2);
    console.log('Разность = ', num1 - num2);
    console.log('Произведение = ', num1 * num2);
});