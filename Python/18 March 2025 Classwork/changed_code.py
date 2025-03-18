# Запустить программу, исправив 3 на 5. Чтобы вопросов было больше. 
# Создать новую программу, которая читает файл и создает словарь. 
# Ключ - вопрос, значение - ВЕРНЫЙ ответ по файлу с верными и неверными ответами. Кому скучно - добавьте дату.


import random

# Функция для сложения
def sum(a, b):  
    return a + b

def div(a, b):  
    return a / b

def mul(a, b):  
    return a * b

# Лямбда-функция для вычитания
sub = lambda a, b: a - b

def generate():
    f = {
        '+': lambda a, b: a + b,
        '-': lambda a, b: a - b,
        '*': lambda a, b: a * b,
        '/': lambda a, b: a / b,
    }
    operation = random.choice(list(f))
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    
    if operation == '/':
        return '%s %s %s' % (num1 * num2, operation, num2), num1
    
    correct = f[operation](num1, num2)
    return '%s %s %s' % (num1, operation, num2), correct

def ask_and_save(total_questions):
    correct_answers = 0
    incorrect_questions = []
    answer_dict = {}  # Словарь для хранения вопросов и правильных ответов

    with open('school_test.txt', 'w', encoding='utf-8') as f:
        for i in range(total_questions):
            question, correct = generate()
            user_answer = input(f'{question} = ')
            f.write(f'{question} = {user_answer} ')

            if user_answer == str(correct):
                f.write('верно\n')
                correct_answers += 1
            else:
                f.write(f'неверно, правильный ответ {correct}\n')
                incorrect_questions.append((question, correct))
                answer_dict[question] = correct  # Добавляем в словарь

    return correct_answers, answer_dict

def re_ask(answer_dict):  # Повторно задаем вопросы, которые были отвечены неверно
    print("Начинаем второй раунд")
    correct_answers = 0

    with open("answer_list.txt", "w", encoding="utf-8") as f_new:
        for question, correct in answer_dict.items():
            user_answer = input(f"{question} = ")
            if user_answer == str(correct):
                f_new.write(f'{question} = {user_answer} верно\n')
                correct_answers += 1
            else:
                f_new.write(f'{question} = {user_answer} неверно, правильный ответ {correct}\n')

    print(f"Второй раунд: задано {len(answer_dict)} вопросов, {correct_answers} из них верно")

def combine_results():
    with open('school_test.txt', 'r', encoding='utf-8') as f1, \
         open('answer_list.txt', 'r', encoding='utf-8') as f2, \
         open('combined_results.txt', 'w', encoding='utf-8') as f_combined:
        
        f_combined.write("Результаты первого раунда:\n")
        f_combined.write(f1.read())
        f_combined.write("\nРезультаты второго раунда:\n")
        f_combined.write(f2.read())

def main():
    total_questions = 5
    correct_answers, answer_dict = ask_and_save(total_questions)
    print(f"Было задано {total_questions} вопросов, {correct_answers} из них верно.")
    print("Задания созданы и записаны в файл 'school_test.txt'.")
    re_ask(answer_dict)
    combine_results()  # Объединяем результаты в один файл

main()