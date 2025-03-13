function BirthdayGreeting() {
    const name = document.getElementById('name').value;
    const surname = document.getElementById('surname').value;
    const yearInput = document.getElementById('year').value;

    const year = Number(yearInput);

    const today = new Date();
    const age = today.getFullYear() - year;
    
    // С данной строкой загвоздка: как определить пол по имени?
    // В данной строке сделано примитивное решение, т.е. если возраст четный, то окончание женское,
    // если нечентное - то мужское.
    // Есть предположение, что нужно составить списки из имен мужских и женских.
    // И исходя из данных списков подбирать окончание, но как-то сложно))

    const endings = ['ой', 'ая'];
    const greeting = `Дорог${endings[age % 2]} ${name} ${surname}, поздравляем Вас с Днем рождения! Вам исполнилось ${age} лет.`;

    alert(greeting); 
}