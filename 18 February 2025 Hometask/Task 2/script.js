let passengerCount = 1; // изначально учитываем одного пассажира
const basePrice = 1000; // возьмем цену за одного пассажира
const bedPrice = 200;   // цена за один комплект белья

function addPassenger() {
    passengerCount++;
    const passengerDiv = document.createElement('div');
    passengerDiv.classList.add('passenger');

// А дальше хоть и работает, но на мой взгляд как-то слишком много и избыточно.
// Вычитал на нескольких форумах пару более "простых" вариантов по типу innerHTML, но не все моменты понял.
// В итоге как в той фразе: слипили из того что было.

    const labels = ['Имя', 'Фамилия', 'Паспорт', 'Вагон', 'Место', 'С бельём'];
    const classes = ['name', 'surname', 'passport', 'carriage', 'seat'];

    labels.forEach((labelText, index) => {
        if (index < 5) {                    // Для первых пяти полей рассматриваем отдельно, так как рассматриваем текстовые поля.
            const label = document.createElement('label');
            label.textContent = labelText + ':';
            passengerDiv.appendChild(label);

            const input = document.createElement('input');
            input.type = 'text';
            input.className = classes[index];
            input.placeholder = labelText;
            input.required = true;
            passengerDiv.appendChild(input);
        } else {                            // Для поля белья
            const label = document.createElement('label');
            label.textContent = labelText + ':';
            passengerDiv.appendChild(label);

            const checkbox = document.createElement('input');
            checkbox.type = 'checkbox';
            checkbox.className = 'withBed';
            checkbox.onchange = updateTotal;
            passengerDiv.appendChild(checkbox);
        }
    });

    document.getElementById('passengerFields').appendChild(passengerDiv);
    updateTotal();
}

// Подсчитываем стоимость данного веселья
function updateTotal() {
    const totalBedCount = document.querySelectorAll('.withBed:checked').length;
    const totalCost = (basePrice * passengerCount) + (totalBedCount * bedPrice);
    document.getElementById('totalCost').innerText = totalCost;
}
