# Task 1

# Открыть файл на запись. На 10: Задавать человеку 20-30 случайных вопросов на вычитание 
# (на 12 - на все 4 действия арифметики с ЦЕЛЫМ делением!), сохранять результат.
# В конце написать: "было задано 28 вопросов, 11 из них верно".

# Для начала священный рандом
import random

# Пишем функцию для генерирования примеров из двух случайных чисел, также указываем список
# арифметических операций, тоже на рандоме. Ну и сохраняем правильный ответ, в зависимости от операции
def generate():
    operation = random.choice(['+', '-', '*', '/'])

    if operation == '+':
        num1 = random.randint(0, 10)
        num2 = random.randint(0, 10)
        correct = num1 + num2
        
    elif operation == '-':
        num1 = random.randint(0, 10)
        num2 = random.randint(0, 10)
        correct = num1 - num2
        
    elif operation == '*':
        num1 = random.randint(0, 10)
        num2 = random.randint(0, 10)
        correct = num1 * num2
    
    # А с делением сильно заморочимся: 
    # первая проблема - деление на ноль невозможно, поэтому границы не (0, 10), а (1, 10).
    # вторая проблема - при делении возможны ситуации 2/7 и тогда плохо. Поэтому решение будет следующим:
    # пусть число один состоит из умножения двух чисел: второго и рандомного. Тогда первое число всегда будет больше 
    # и будет полностью сокращаться со знаменателем
    elif operation == '/':
        num2 = random.randint(1, 10)
        num1 = num2 * random.randint(1, 10)
        correct = num1 // num2      
        
    return num1, num2, operation, correct


f = open('school_test.txt', 'w', encoding='utf-8')

# Очень важно обнулить наш счетчик правильных ответов и указать общее число вопросов
correct_answers = 0
total_questions = 20

# Генерируем 20 заданий
for i in range(total_questions):
    num1, num2, operation, correct = generate()
    user_answer = int(input(f'{num1} {operation} {num2} = '))

    if user_answer == correct:
        f.write(f'{num1} {operation} {num2} = {user_answer} верно\n')
        correct_answers += 1
        
    else:
        f.write(f'{num1} {operation} {num2} = {user_answer} неверно, правильный ответ {correct}\n')

f.close()


print(f"Было задано {total_questions} вопросов, {correct_answers} из них верно.")
print("Задания созданы и записаны в файл 'school_test.txt'.")

# ------------------------------------------------------------------------------------------------------------------------------------------ #

# Task 2

# Открыть файл с вопросами на чтение. Задать человеку повторно вопросы, на которые он не смог ответить. 
# Присоединить к старому файлу новый результат.