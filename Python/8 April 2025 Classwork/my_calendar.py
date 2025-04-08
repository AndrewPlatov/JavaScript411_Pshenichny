class MyCalendar:
    
    def __init__(self, year, month=1, day=1):
        self.__year = year
        self.__month = month
        self.__day = day

    @property
    def leap(self):
        # Проверка на високосный год
        return (self.__year % 4 == 0 and self.__year % 100 != 0) or (self.__year % 400 == 0)

    @property
    def year(self):
        return self.__year
    
    @property
    def day(self):
        return self.__day
    
        # Функция, не меняющая поля класса!
    def days_in_month(self, month_number):  # 1..12
        if month_number in [4, 6, 9, 11]:
            # Апрель, Июнь, Сентябрь, Ноябрь
            return 30
        elif month_number == 2:
            if self.leap:
                # Високосный Февраль
                return 29
            # Невисокосный Февраль
            return 28
        return 31

    def set_day(self, new_day):
        if isinstance(new_day, int):
            # Убедились, что перед нами - целое число,
            if 0 < new_day <= self.days_in_month(self.__month):
                # не меньше 1 и не больше числа дней в ЭТОМ месяце
                self.__day = new_day
            else:
                print('Неверный номер дня %i для меяца %i' % (
                    new_day, self.__month))
        else:
            print('Неверно, день должен быть числом, а не %s!' % new_day)

mc = MyCalendar(2025, 6, 29)
mc.set_day(54)
mc.set_day('My birthday')
mc.set_day(2)
print(mc)