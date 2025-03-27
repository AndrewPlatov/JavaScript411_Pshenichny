from datetime import datetime, timedelta

class Task:
    def __init__(self, description, deadline=datetime.now() + timedelta(1)):
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

# Исходник
dress = Task('Сшить джинсовое платье из обрезков')
print('Что сделать: ', dress.description)
print('Когда поставлена? ', dress.dt)
print('К какому сроку? ', dress.deadline)
print('Сделано? ', dress.done)

# Установка нового описания и дедлайна
dress.set_description('К черту платье, делаем плед!')
dress.set_deadline(datetime.now() + timedelta(7))
print('Новое описание: ', dress.description)
print('Новый срок: ', dress.deadline)

# Проверка оставшихся дней и часов после изменения дедлайна
print('Осталось дней до дедлайна: ', dress.days_deadline())
print('Осталось часов до дедлайна: ', dress.hours_deadline())

# Проверка оставшихся дней и часов
print('Осталось дней до дедлайна: ', dress.days_deadline())
print('Осталось часов до дедлайна: ', dress.hours_deadline())
print('Сколько дней было дано на задачу: ', dress.days_given())

# Завершение задачи
dress.complete()
print('Сделано? ', dress.done)
