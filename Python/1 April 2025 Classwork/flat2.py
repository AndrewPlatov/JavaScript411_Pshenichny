# Написать функцию, которая вычисляет площадь квартиры. 
# Квартира - массив словарей {"ширина": 5, "длина": 3}

def calculate_area(rooms):
    totals = 0
    
    for room in rooms:
        width = room["ширина"]
        length = room["длина"]
        
        room_area = width * length
        
        totals += room_area
    
    return totals

rooms = [
    {"ширина": 5, "длина": 3},  # Комната 1
    {"ширина": 4, "длина": 4},  # Комната 2
    {"ширина": 6, "длина": 2}   # Комната 3
]
    
area = calculate_area(rooms)
    
print(f"Площадь квартиры: {area} кв. м.")