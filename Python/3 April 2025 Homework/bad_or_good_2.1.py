# Напишите функцию замены bad на good. Используйте ord и chr, стыдно алфавит руками вбивать.

# Хорошенько подумав, решил что можно без ord и chr. Даже немного проще и читабельнее, на мой взгляд...

def replace_bad_with_good(text):
    bad = "bad"
    good = "good"
    bad_length = len(bad)       # Определяем длину слова 'bad'
    
    # Создаем список для результата
    result = []
    
    i = 0
    while i < len(text):
        # Проверяем, совпадает ли текущая подстрока с 'bad'
        if (i + bad_length <= len(text) and text[i:i + bad_length] == bad):
            # Проверяем границы слова
            if (i == 0 or text[i - 1] in [' ', '.', ',', ':', ';', '@', '!', '?']) and (i + bad_length == len(text) or text[i + bad_length] in [' ', '.', ',', ':', ';', '@', '!', '?']):
                # Если совпадает и это отдельное слово, добавляем 'good' в результат
                result.extend([ord(c) for c in good])
                i += bad_length  # Пропускаем длину 'bad'
            else:
                # Если не отдельное слово, просто добавляем текущий символ
                result.append(ord(text[i]))
                i += 1
        else:
            # Если не совпадает, добавляем текущий символ в результат
            result.append(ord(text[i]))
            i += 1  # Переходим к следующему символу
    
    # Преобразуем список кодов обратно в строку
    return ''.join(chr(c) for c in result)

input_text1 = "I'm a bad girl."
output_text1 = replace_bad_with_good(input_text1)
print(output_text1)  

input_text2 = "This is a bad example of a bad function."
output_text2 = replace_bad_with_good(input_text2)
print(output_text2) 

input_text3 = "I love badminton."
output_text3 = replace_bad_with_good(input_text3)
print(output_text3)