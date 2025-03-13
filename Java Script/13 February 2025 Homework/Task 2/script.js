function createButtonTable() {
    const tableContainer = document.getElementById('table-container');

    const table = document.createElement('table');

    for (let i = 0; i < 5; i++) { 
        const row = document.createElement('tr');

        for (let j = 0; j < 5; j++) { 
            const cell = document.createElement('td');
            const button = document.createElement('button');

            button.innerText = `Кнопка ${i * 5 + j + 1}`;
            button.onclick = function() {
                cell.removeChild(button); 
                const message = document.createElement('span');
                message.innerText = ' boom 💥 ';
                cell.appendChild(message); 
            };

            cell.appendChild(button); 
            row.appendChild(cell); 
        }

        table.appendChild(row); 
    }

    tableContainer.appendChild(table);
}

createButtonTable();