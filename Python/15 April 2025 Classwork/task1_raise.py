import datetime

def get_birth_year():
    current_year = datetime.datetime.now().year
    num1 = None

    while num1 is None:
        try:
            num1 = int(input("Введите год рождения: "))
            if num1 > current_year:
                raise ValueError(f"Год не должен превышать {current_year}.")
            elif num1 < 1900:
                raise ValueError("Год рождения не может быть меньше 1900.")
        except ValueError:
            print("Некорректный ввод. Пожалуйста, введите число в диапазоне от 1900 до {current_year}.")
            num1 = None

    return num1

year_of_birth = get_birth_year()
print(f"Год рождения: {year_of_birth}")