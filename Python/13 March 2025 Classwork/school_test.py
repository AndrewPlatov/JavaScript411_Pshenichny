# Теперь создадим файл и запишем туда вопросы и ответы первоклашек. 
# Вопрос - задание на сложение в пределах 20 (т.е. каждое слагаемое не больше 10, или...?), 
# ответ надо проверить и дать верный, если человек ошибся. Например:
# 5 + 3 = 8 верно
# 8 + 2 = 11 неверно, 10

# Для начала священный рандом
import random

# Пишем функцию для генерирования примеров из двух случайных чисел и сохраняем верный ответ
def generate():
    num1 = random.randint(0, 10)
    num2 = random.randint(0, 10)
    correct = num1 + num2
    return num1, num2, correct


f = open('school_test.txt', 'w', encoding='utf-8')

# Генереируем 10 заданий
for i in range(10):
    num1, num2, correct = generate()
    user_answer = int(input(f'{num1} + {num2} = '))
    if user_answer == correct:
        f.write(f'{num1} + {num2} = {user_answer} верно\n')
    else:
        f.write(f'{num1} + {num2} = {user_answer} неверно, {correct}\n')

f.close()

print("Задания на сложение созданы и записаны в файл 'school_test.txt'.")