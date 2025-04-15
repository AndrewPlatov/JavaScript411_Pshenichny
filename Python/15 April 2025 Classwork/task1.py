# Программа спрашивает год рождения. Необходимо учесть, что помимо
# года рождения может быть введён любой мусор. Дождаться
# корректного ввода, не используя функцию isdigit

def birth_year():
    while True:
        user_input = input("Введите год рождения: ")
        try:
            birth = int(user_input)
            return birth
        except ValueError:
            print("Некорректный ввод. Пожалуйста, введите год рождения ЧИСЛОМ.")

year_of_birth = birth_year()
print(f"Ваш год рождения: {year_of_birth}")