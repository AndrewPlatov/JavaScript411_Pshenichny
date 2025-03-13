const form = document.getElementById('userForm');
const reportDiv = document.getElementById('report');

form.addEventListener('submit', function(event) {
    // Вычитал, что для более корректной работы форм можно использовать preventDefault.
    // Как я понял, оно используется для того, чтобы форма не перезагружалась и пользователь не менял данные.
    // Это нужно чтобы корректно выгрузить данные из формы для дальнейшей обработки.
    event.preventDefault();

    // Нужно получить (выгрузить) данные из формы для формирования отчета:
    const firstName = document.getElementById('firstName').value;
    const lastName = document.getElementById('lastName').value;
    const birthYear = Number(document.getElementById('birthYear').value, 10);
    const currentDate = new Date(document.getElementById('currentDate').value);

    const currentYear = currentDate.getFullYear();
    const age = currentYear - birthYear;

    // Только есть недочет, который не получается исправить: отчет всегда формируется в 3 ночи.
    // Без понятия как это исправить и учитывать текущее время в отчете.
    const report = `Я - ${firstName} ${lastName}. В ${currentYear + age} году мне будет ${age} лет. Расчет произведен ${currentDate.toLocaleDateString('ru-RU')} в ${currentDate.toLocaleTimeString('ru-RU')}.`;

    // Просто скрываем форму или можно использовать form.remove() для удаления формы.
    form.style.display = 'none'; 

    reportDiv.style.display = 'block';
    reportDiv.textContent = report;
});