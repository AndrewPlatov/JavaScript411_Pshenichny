const calculateButton = document.getElementById('calculateButton');

function calculateSum() {
            
    const num1 = Number(document.getElementById('number1').value);
    const num2 = Number(document.getElementById('number2').value);

    const sum = num1 + num2;

    console.log('Сумма:', sum);
}

calculateButton.addEventListener('click', calculateSum);