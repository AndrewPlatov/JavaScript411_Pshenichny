# Task 3
# Написать свой класс для хранения информации о единице одежды: тип, фирма, цвет

class ClothInfo:
    def __init__(self, form="T-shirt", brand="Nike", color="Red", amount=10):
        self.form = form
        self.brand = brand
        self.color = color
        self.amount = amount
        
cin = ClothInfo()
print(cin.amount, cin.form, cin.color, cin.brand)
