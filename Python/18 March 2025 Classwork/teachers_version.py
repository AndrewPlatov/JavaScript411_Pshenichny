# Открыть файл на запись. 
# Задавать человеку 20-30 случайных вопросов на +-*/ 
# При делении должны получаться целые числа! 
# сохранять результат.
# В конце написать: "было задано 28 вопросов, 11 из них верно".

# Для начала священный рандом
import random

# Функция с именем
def sum(a, b):  return a + b
# function sum(a, b) {return a + b}
#def sub(a, b):  return a - b
def div(a, b):  return a / b
def mul(a, b):  return a * b

# lambda - безымянная, "стрелочная" функция 
sub = lambda a, b : a - b
# (a, b) => a + b

def generate():
    f = {
        '+': lambda a, b: a + b,  # Значение - функция суммы
        '-': lambda a, b: a - b,  # Значение - функция разности
        '*': lambda a, b: a * b,
        '/': lambda a, b: a / b,
    }
    # Выбрать оператор (действие арифметики)
    operation = random.choice(list(f)) # '+-*/')
    # opi = random.randint(0,4)  # номер оператора
    # op = '+-*/'[opi]           # выбираем знак арифметики
    # Выбрать первое число # Выбрать второе число
    num1 = random.randint(1, 10)  # 7
    num2 = random.randint(1, 10)  # 5
    #if operation == '+':
    #    correct = num1 + num2
    #            '+'  =>   sum(num1, num2)
    if operation == '/':   # result / num1 = num2
        #      35 / 5, 7
        return '%s %s %s' % (num1 * num2, operation, num2), num1   
    correct = f[operation](num1, num2)
    # Вернуть вопрос и ответ
    return '%s %s %s' % (num1, operation, num2), correct

# Создаем функцию с одним параметром
def ask_and_save(total_questions):
    # Очень важно обнулить наш счетчик правильных ответов
    correct_answers = 0       # количество верных ответов
    incorrect_questions = []  # список неверных ответов

    f = open('school_test.txt', 'w', encoding='utf-8')

    # Генерируем задания
    for i in range(total_questions):
        # for i in range(50) - цикл. Повторить 50 раз
        question, correct = generate()
        user_answer = input(f'{question} = ')  # Задали вопрос пользователю и дождались ответа
        f.write(f'{question} = {user_answer} ')

        if user_answer == str(correct):
            f.write('верно\n')
            correct_answers += 1
        
        else:
            f.write(f'неверно, правильный ответ {correct}\n')
            incorrect_questions.append((question, correct))
            
    f.close()
    return correct_answers

def re_ask():  # Повторно задаем вопросы, которые были отвечены неверно
    print("Начинаем второй раунд")

    f = open("school_test.txt", "r", encoding="utf-8")

    f_new = open("answer_list.txt", "w", encoding="utf-8")
            
    i = 0
    for line in f:
        if "неверно" in line:
            i += 1
            # Из-за использования файла ещё и на запись, пока пользователь
            # не ответит верно на все, программа не окончится!
            #f = open("answer_list.txt", "a", encoding="utf-8")
            correct_answers = 0
            #7 + 3 = 8 неверно, 10
            question, answers = line.split(' = ')  # ['7 + 3', '8 неверно, 10']
            wrong, correct = answers.split(' неверно, правильный ответ ')
            #correct = correct.split()[0]
            correct = correct.strip()  # Сбросить справа и слева все пробельные символы
            user_answer = input(f"{question} = ")
            print('"%s"' % user_answer)
            print('"%s"' % correct)
            if user_answer == correct:
                f_new.write(f'{question} = {user_answer} верно\n')
                correct_answers += 1
            else:
                f_new.write(f'{question} = {user_answer} неверно, правильный ответ {correct}\n')
    
    f_new.close()
    print(f"Второй раунд: задано {i} вопросов, {correct_answers} из них верно")
    f.close()  
 

def main():
    total_questions = 3
    correct_answers = ask_and_save(total_questions)
    print(f"Было задано {total_questions} вопросов, {correct_answers} из них верно.")
    print("Задания созданы и записаны в файл 'school_test.txt'.")
    re_ask()

main()