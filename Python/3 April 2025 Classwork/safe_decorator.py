def safe_call(func):
    def call(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except:
            print("Произошла ошибка при вызове функции")
            return None  
    return call

@safe_call
def div(a, b):
    return a / b

# Функция с ошибкой
result = div(10, 0)  # Это вызовет ошибку деления на ноль
print(result)

# Функция без ошибки
result = div(10, 2)
print(result)