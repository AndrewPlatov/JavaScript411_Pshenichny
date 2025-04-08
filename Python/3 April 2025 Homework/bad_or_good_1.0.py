# Напишите функцию замены bad на good. Используйте ord и chr, стыдно алфавит руками вбивать.

def replace_bad_with_good(text):
    # Определяем символы для замены
    bad = "bad"
    good = "good"
    
    # Получаем длину слова 'bad'
    bad_length = len(bad)
    
    # Создаем список для результата
    result = []
    
    i = 0
    while i < len(text):
        # Проверяем, совпадает ли текущая подстрока с 'bad'
        if text[i:i + bad_length] == bad:
            # Если совпадает, добавляем 'good' в результат
            result.extend(good)
            i += bad_length  # Пропускаем длину 'bad'
        else:
            # Если не совпадает, добавляем текущий символ в результат
            result.append(text[i])
            i += 1  # Переходим к следующему символу
    
    # Преобразуем список обратно в строку
    return ''.join(result)

input_text1 = "I'm a bad girl."
output_text1 = replace_bad_with_good(input_text1)
print(output_text1)

input_text2 = "This is a bad example of a bad function."
output_text2 = replace_bad_with_good(input_text2)
print(output_text2)

input_text3 = "I love badminton."
output_text3 = replace_bad_with_good(input_text3)
print(output_text3)