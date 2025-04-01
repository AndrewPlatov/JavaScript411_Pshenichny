# Написать функцию, которая вычисляет площадь квартиры. 
# Квартира - массив пар "ширина, длина" для каждой комнаты.

def square_area(rooms):
    total_area = 0
    for width, length in rooms:
        total_area += width * length
    return total_area

rooms = [(5, 3), (4, 4), (6, 2)]  
area = square_area(rooms)
    
print(f"Площадь квартиры: {area} кв. м.")



