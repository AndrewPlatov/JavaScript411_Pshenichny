// Task 4
// Класс Книга: Название, автор, год издания, содержание книги (пример! не надо всю копировать! Можно "Репку" в качестве примера...) 

// Для начала как и в PYTHON создадим свой класс (название, автор, год издания, краткое содержание, собственное мнение)
class Book {
    constructor(name, author, year, briefly, opinion) {
        this.name = name;
        this.author = author;
        this.year = year;
        this.briefly = briefly;
        this.opinion = opinion;
    }

    // Создаем строки таблицы
    toTableRow() {
        // Создаем элемент строки
        const row = document.createElement('tr');

        // Создаем ячейки и добавляем данные
        const nameCell = document.createElement('td');
        nameCell.textContent = this.name;
        row.appendChild(nameCell);

        const authorCell = document.createElement('td');
        authorCell.textContent = this.author;
        row.appendChild(authorCell);

        const yearCell = document.createElement('td');
        yearCell.textContent = this.year;
        row.appendChild(yearCell);

        const brieflyCell = document.createElement('td');
        brieflyCell.textContent = this.briefly;
        row.appendChild(brieflyCell);

        const opinionCell = document.createElement('td');
        opinionCell.textContent = this.opinion;
        row.appendChild(opinionCell);

        return row; // Возвращаем созданную строку и так варить до готовности
    }
}

// По аналогии с PYTHON создаем три класса Book с данными
const book1 = new Book("1984", "Джордж Оруэлл", 1949, "Дистопия о тоталитарном обществе.", "Как лечить алкоголизм курением");
const book2 = new Book("Война и мир", "Лев Толстой", 1869, "Эпопея о жизни русского общества во время Наполеоновских войн.", "Очень долго, но невероятно захватывает");
const book3 = new Book("Квантовая механика", "Альберт Месси", 1958, "Основы квантовой механики и её применение в физике.", "Я понял, что я ничего не понял");

// Получаем элемент tbody для добавления строк
const bookTableBody = document.getElementById('book-table-body');

// Добавляем строки в таблицу
bookTableBody.appendChild(book1.toTableRow());
bookTableBody.appendChild(book2.toTableRow());
bookTableBody.appendChild(book3.toTableRow());
