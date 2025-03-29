from datetime import datetime, timedelta

class Task:
    def __init__(self, description, deadline=datetime.now() + timedelta(100)):      # увеличу дельту с 1 до 100 дней, чтобы захватить праздники
        self.dt             = datetime.now()  # Когда задача была поставлена
        self.deadline       = deadline        # Срок, к которому задачу надо сделать
        self.description    = description     # Описание. Подробное и понятное
        self.done           = False           # Сделана или нет?


    # Делает задачу завершённой
    def complete(self):
        self.done = True

    # Устанавливает новое описание.
    def set_description(self, new_description):
        self.description = new_description

    # Устанавливает новый дедлайн
    def set_deadline(self, new_deadline):
        self.deadline = new_deadline

    # Проверяет, сколько осталось дней до срока выполнения?
    def days_deadline(self):
        return (self.deadline - datetime.now()).days

    # Проверяет, сколько осталось часов до срока выполнения?
    def hours_deadline(self):
        return (self.deadline - datetime.now()).seconds // 3600

    # Сколько дней было дано на задачу?
    def days_given(self):
        return (self.deadline - self.dt).days


# Проверим, сколько рабочих дней (без выходных и празников) было дано на задачу
    def working_days_given(self, holidays=[]):
        total_days = 0
        current_date = self.dt

        while current_date < self.deadline:
            # Проверяем, является ли текущая дата выходным или праздником. 
            # Указываем число 5, так как оно будет невключительно, то есть: 0-4: Пн-Пт
            # А праздники прийдется задавать вручную =(
            if current_date.weekday() < 5 and current_date not in holidays:
                total_days += 1
            current_date += timedelta(days=1)

        return total_days

# Например возьмем ряд праздников
holidays = [
    datetime(2025, 1, 1),    # Новый год
    datetime(2025, 5, 1),    # Первое мая
    datetime(2025, 5, 9),    # Девятое мая
    datetime(2025, 6, 12),   # 12 июня
    datetime(2025, 12, 25),  # Рождество
]


# Исходник
dress = Task('Сшить джинсовое платье из обрезков')
print('Что сделать: ', dress.description)
print('Когда поставлена? ', dress.dt)
print('К какому сроку? ', dress.deadline)
print('Сделано? ', dress.done)

# Установка нового описания и дедлайна
dress.set_description('К черту платье, делаем плед!')
dress.set_deadline(datetime.now() + timedelta(107))   # раз увеличил до 100 лней дельту в начале, тут увеличу на 107
print('Новое описание: ', dress.description)
print('Новый срок: ', dress.deadline)

# Проверка оставшихся дней и часов
print('Осталось дней до дедлайна: ', dress.days_deadline())
print('Осталось часов до дедлайна: ', dress.hours_deadline())
print('Сколько дней было дано на задачу: ', dress.days_given())

# Показываем рабочие дни:
print('Сколько рабочих дней было дано на задачу: ', dress.working_days_given(holidays))

# Завершение задачи
dress.complete()
print('Сделано? ', dress.done)
