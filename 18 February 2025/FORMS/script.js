function colorize() {
    if (anq.gender.value == "female") {
        anq.style.backgroundColor = "#FFAB90"
    } else if (anq.gender.value == "male") {
        anq.style.backgroundColor = "#90ABFF"
    } else {
        anq.style.backgroundColor = "#39a845"
    }
}

// Ищем возраст:
function calculateAge() {
    const birthInput = document.getElementById('birth');
    const birth = new Date(birthInput.value);
    const today = new Date();

    const age = today.getFullYear() - birth.getFullYear();

    alert("Ваш возраст: " + age + " лет");
}

// Только есть проблема: при вводе с клавиатуры программа реагирует только на первую цифру
// и сразу выдает возраст. При вводе 1 сразу пишет "возраст 2024", т.е. не дает ввести 1998