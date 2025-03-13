# Текстовые файлы

# Task 1

f = open('my_tasks.txt', 'w', encoding='utf-8')
f.write("Жила-была мама. Она мыла раму.")
f.flush()
f.close()

tasks = [
    "Отработка записи:",
    "Создать папку с сегодняшней датой",
    "Создать в ней питонный файл (программу)",
    "Выполнить программу, написанную на 1-м слайде",
    "Убедиться, что появился файл",
    "Создать новую программу, которая пишет в файл 'my_tasks.txt' список вышеуказанных действий"
]

f = open('my_tasks2.txt', 'a', encoding='utf-8')
for i, task in enumerate(tasks, start=1):
    f.write(f'{i}. {task}\n')
f.close()

# ------------------------------------------------------------------------------------------------------------------------------------------ #