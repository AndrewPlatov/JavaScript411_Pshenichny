function createAdditionTable() {
    const tableContainer = document.getElementById('table-container');

    const table = document.createElement('table');

    const headerRow = document.createElement('tr');
    const headerCell = document.createElement('th');
    headerCell.innerText = ' + ';
    headerRow.appendChild(headerCell);

    for (let i = 1; i <= 10; i++) {
        const headerCell = document.createElement('th');
        headerCell.innerText = i;
        headerRow.appendChild(headerCell);
    }
    table.appendChild(headerRow);

    for (let i = 1; i <= 10; i++) {
        const row = document.createElement('tr');

        const rowHeader = document.createElement('th');
        rowHeader.innerText = i;
        row.appendChild(rowHeader);

        for (let j = 1; j <= 10; j++) {
            const cell = document.createElement('td');
            cell.innerText = i + j; 
            row.appendChild(cell);
        }

        table.appendChild(row); 
    }

    tableContainer.appendChild(table);
}

createAdditionTable();