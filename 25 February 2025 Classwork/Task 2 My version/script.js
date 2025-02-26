// РАБОЧАЯ ВЕРСИЯ НИЖЕ, БЫЛО ЖАЛКО СНОСИТЬ КОД

// Версия 1. Но тут не получилось окрасить ячейки (((

// function createSeasonTable() {
//     const table = document.createElement('table');
//     const seasons = ['Весна', 'Лето', 'Осень', 'Зима'];
//     const monthsArray = [
//         ['Март', 'Апрель', 'Май'],
//         ['Июнь', 'Июль', 'Август'],  
//         ['Сентябрь', 'Октябрь', 'Ноябрь'], 
//         ['Декабрь', 'Январь', 'Февраль']  
//     ];

//     for (let i = 0; i < seasons.length; i++) {
//         const tr = document.createElement('tr');
//         const seasonCell = document.createElement('td');
//         seasonCell.textContent = seasons[i];
//         tr.appendChild(seasonCell);

//         for (let month of monthsArray[i]) {
//             const td = document.createElement('td');
//             td.textContent = month;
//             tr.appendChild(td);
//         }

//         table.appendChild(tr);
//     }

//     document.getElementById('seasonTable').appendChild(table);
// }

// createSeasonTable();

// --------------------------------------------------------------------------------------- //

// Версия 2. Тут получилось окрасить, но не совсем как у Вас: 

function createSeasonTable() {
    const table = document.createElement('table');
    
    const seasons = ['Весна', 'Лето', 'Осень', 'Зима'];
    const monthsArray = [
        ['Март', 'Апрель', 'Май'],    
        ['Июнь', 'Июль', 'Август'],   
        ['Сентябрь', 'Октябрь', 'Ноябрь'], 
        ['Декабрь', 'Январь', 'Февраль']  
    ];

    const headerRow = document.createElement('tr');
    const headerCell1 = document.createElement('th');
    headerCell1.textContent = 'Сезон';
    const headerCell2 = document.createElement('th');
    headerCell2.textContent = 'Месяцы';
    
    headerRow.appendChild(headerCell1);
    headerRow.appendChild(headerCell2);
    table.appendChild(headerRow);

    for (let i = 0; i < seasons.length; i++) {
        const tr = document.createElement('tr');

        const seasonCell = document.createElement('td');
        seasonCell.textContent = seasons[i];
        seasonCell.className = seasons[i]; 
        tr.appendChild(seasonCell);
        
        const monthCell = document.createElement('td');
        monthCell.textContent = monthsArray[i].join(', '); 
        tr.appendChild(monthCell);

        table.appendChild(tr);
    }

    document.getElementById('seasonTable').appendChild(table);
}

createSeasonTable();