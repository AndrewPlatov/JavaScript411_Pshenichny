def categorize_flats(flats_list):
    categorized_flats = {
        1: [],
        2: [],
        3: []
    }
    
    for flat in flats_list:
        rooms = flat.get("количество_комнат")
        
        if rooms in categorized_flats:
            categorized_flats[rooms].append(flat)
    
    return categorized_flats


flats = [
    {"адрес": "ул. Ленина, д.1", "количество_комнат": 2},
    {"адрес": "ул. Пушкина, д.2", "количество_комнат": 3},
    {"адрес": "ул. Тверская, д.5", "количество_комнат": 1}
]
    
categorized = categorize_flats(flats)
    
print("Категоризация квартир:")

for room_count, flats in categorized.items():
    print(f"{room_count}-комнатные квартиры: {flats}")
    
def save_to_file(among_flats, content):
    f = open(among_flats, mode='w', encoding='utf-8')
    f.write(content)
    f.close