class ShoppingInfo:
    def __init__(self, description, form, brand, color, price = "", amount = None):
        self.description = description
        self.form = form
        self.brand = brand
        self.color = color
        self.price = price
        self.amount = amount
    
    def __str__(self):
        return (f"Шоппинг:\n"
                f"Описание: {self.description}\n"
                f"Тип одежды: {self.form}\n"
                f"Брэнд: {self.brand}\n"
                f"Цвет: {self.color}\n"
                f"Цена: {self.price}\n"
                f"Количество: {self.amount}")
    
    # Устанавливает новое описание.
    def set_description(self, new_description):
        self.description = new_description

shopping = ShoppingInfo(description = "Получить серотонин", form = "Костюм", brand = "Gucci", color = "black", price = "10.000 $", amount = "1")
print(shopping)
print()

# Установка нового описания и дедлайна
shopping.set_description('Не потрать все деньги !')
print('Новое описание: ', shopping.description)
print()

shopping2 = ShoppingInfo(description = "Модник", form = "Рубашка", brand = "Versace", color = "pink",)
print(shopping2)