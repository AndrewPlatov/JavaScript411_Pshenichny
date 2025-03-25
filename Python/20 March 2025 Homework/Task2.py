# Записать новый файл, в котором фамилии будут каждая на новой строке.

# Читаем фамилии из файла Task1 subbotnik.txt
with open('subbotnik.txt', 'r', encoding='utf-8') as file:
    surnames = file.read().strip().split(',')

# Записываем фамилии в новый файл new_subbotnik.txt, каждая на новой строке
with open('new_subbotnik.txt', 'w', encoding='utf-8') as file:
    for surname in surnames:
        file.write(surname + '\n')                              # добавляем новую строку после каждой фамилии