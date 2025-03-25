// Task 1
// Написать свой класс для хранения информации о человеке: фамилия, имя, отчество, дата рождения

class MenInfo {
    constructor(name, surname, patronymic, year, height) {
        this.name = name;
        this.surname = surname;
        this.patronymic = patronymic;
        this.year = year;
        this.height = height;
    }

    calculateAge() {
        const currentYear = new Date().getFullYear();
        return currentYear - this.year;
    }
}

const mi = new MenInfo("Андрей", "Пшеничный", "Михайлович", 1998, 171);

console.log(mi.name);
console.log(mi.surname);
console.log(mi.patronymic);
console.log(mi.year);
console.log(mi.calculateAge());