function Grades() {
    const grades = {};
    const startDate = new Date(2023, 0, 1); // Январь - это месяц 0
    for (let i = 0; i < 20; i++) {
        const date = new Date(startDate);
        date.setDate(startDate.getDate() + i);
        const formattedDate = date.toLocaleDateString('ru-RU'); // Форматируем дату
        grades[formattedDate] = Math.floor(Math.random() * 6) + 7; // Генерация оценок от 7 до 12
    }

    displayGrades(grades);

    const averageAll = calculateAverage(grades);
    document.getElementById('averageAll').textContent = averageAll.toFixed(2);

    const gradesInPeriod = Object.fromEntries(
        Object.entries(grades).filter(([date]) => {
            const d = new Date(date);
            return d >= new Date(2023, 0, 4) && d <= new Date(2023, 0, 9);
        })
    );

    const averagePeriod = calculateAverage(gradesInPeriod);
    document.getElementById('averagePeriod').textContent = averagePeriod.toFixed(2);
}

function displayGrades(grades) {
    const tbody = document.getElementById('gradesTable').querySelector('tbody');
    tbody.innerHTML = ''; // Очистка предыдущих данных
    for (const [date, grade] of Object.entries(grades)) {
        const row = document.createElement('tr');
        row.innerHTML = `<td>${date}</td><td>${grade}</td>`;
        tbody.appendChild(row);
    }
}

function calculateAverage(grades) {
    const values = Object.values(grades);
    if (values.length === 0) return 0;
    const sum = values.reduce((acc, val) => acc + val, 0);
    return sum / values.length;
}