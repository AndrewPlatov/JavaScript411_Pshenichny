# LookupError: KeyError, IndexError
#arr = {}
#arr[0]

# AssertionError: когда ложь!
# assert 0
# assert []
# assert ''
# assert [False]

# AttributeError
#class M:
#
#    b = 0
#
#m = M()
#m.a

# ModuleNotFoundError(ImportError)
# import kuku

# KeyboardInterrupt - прерывание с клавиатуры (Ctrl+C)
# while True:
#     pass
# Запустите и когда оно "повиснет", нажмите контрол-цэ!

# MemoryError не будет. Просто зависнет комп )
#a = 'kuku'
#while True:
#    a *= 2

# NameError: name 'mew' is not defined
# print(mew)


# RecursionError: maximum recursion depth exceeded
# def f():
#     f()
# f()
# Скорее всего, не предусмотрен НЕРЕКУРСИВНЙ случай в функции

# TypeError: unsupported operand type(s) for +: 'int' and 'str'
# 5 + '5'

# FileNotFoundError: [Errno 2] No such file or directory: 'mew.txt'
# open('mew.txt')
try:
    age = int(input('Сколько тебе лет?'))
except ValueError:
    print('Пиши цифрами')