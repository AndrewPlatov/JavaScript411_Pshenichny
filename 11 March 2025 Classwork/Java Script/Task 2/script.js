// Есть три кортежа целых чисел необходимо найти элементы, которые уникальны для каждого списка.

// Определяем три массива целых чисел
const tuple1 = [1, 2, 3, 4, 5];
const tuple2 = [1, 2, 0, 4, 6];
const tuple3 = [1, 0, 3, 7, 8];

// Находим уникальные элементы для первого массива
const unique1 = tuple1.filter(element => 
    !tuple2.includes(element) && !tuple3.includes(element)
);

// Находим уникальные элементы для второго массива
const unique2 = tuple2.filter(element => 
    !tuple1.includes(element) && !tuple3.includes(element)
);

// Находим уникальные элементы для третьего массива
const unique3 = tuple3.filter(element => 
    !tuple1.includes(element) && !tuple2.includes(element)
);

// Выводим результат по каждому
console.log("Уникальные элементы для tuple1:", unique1);
console.log("Уникальные элементы для tuple2:", unique2);
console.log("Уникальные элементы для tuple3:", unique3);