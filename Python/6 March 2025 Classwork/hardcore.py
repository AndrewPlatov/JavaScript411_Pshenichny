# Задано плоское поле единиц и нулей, например:
# [[1, 1, 1], [1, 0, 1],[1, 1, 1]]
# Найти максимальный квадрат из единиц и нарисовать на том же поле только его

def maximal_square(matrix):
    if not matrix:
        return 0

    rows, cols = len(matrix), len(matrix[0])
    dp = [[0] * cols for _ in range(rows)]
    max_side = 0
    max_i = 0
    max_j = 0

    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 1:
                if i == 0 or j == 0:
                    dp[i][j] = 1  # Первый ряд или первый столбец
                else:
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
                
                if dp[i][j] > max_side:
                    max_side = dp[i][j]
                    max_i = i
                    max_j = j

    # Отображаем максимальный квадрат на исходной матрице
    for i in range(max_i - max_side + 1, max_i + 1):
        for j in range(max_j - max_side + 1, max_j + 1):
            matrix[i][j] = 'X'  # Заменяем единицы на 'X' для отображения

    return max_side, matrix

def main():
    # Ввод размеров поля
    rows = int(input("Введите количество строк: "))
    cols = int(input("Введите количество столбцов: "))

    # Ввод элементов поля
    matrix = []
    print("Введите элементы поля (0 или 1):")
    for i in range(rows):
        row = list(map(int, input(f"Строка {i + 1}: ").strip().split()))
        if len(row) != cols or any(x not in (0, 1) for x in row):
            print("Ошибка: Ввод должен содержать только 0 или 1 и соответствовать указанному количеству столбцов.")
            return
        matrix.append(row)

    # Находим максимальный квадрат
    max_square_size, updated_field = maximal_square(matrix)

    # Вывод результата
    print(f"Размер максимального квадрата: {max_square_size}")
    print("Обновленное поле:")
    for row in updated_field:
        print(row)

# Запуск программы
main()