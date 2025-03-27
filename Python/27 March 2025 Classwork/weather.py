# Написать класс "Погода" с полями "солнечно или нет", "температура", "дождь, снег, туман...." - осадки. 
# Если осадков нет, - пусто. Дата, время. Сделать у этого класса инициализатор, который принимает необходимые параметры, 
# причем, если не передать дату и время - возьмет текущие, если не передать солнечно, будет пасмурно, если не передать осадки, 
# будет пусто. Температура является ОБЯЗАТЕЛЬНЫМ параметром.

from datetime import datetime

class Weather:
    def __init__(self, temperature, is_sunny=False, osadki="", date=None, time=None):
        if temperature is None:
            raise ValueError("Температура является обязательной !")
        
        self.temperature = temperature
        self.is_sunny = is_sunny
        self.osadki = osadki
        self.date = date or datetime.now().date()
        self.time = time or datetime.now().time()

    def __str__(self):
        sunny_status = "Солнечно" if self.is_sunny else "Пасмурно"
        osadki_status = self.osadki or "Нет осадков"
        return (f"Дата: {self.date}, Время: {self.time},"
                f"Температура: {self.temperature}°C,"
                f"{sunny_status}, Осадки: {osadki_status}")


weather1 = Weather(20)
print(weather1)

weather2 = Weather(18, is_sunny=True, osadki="Дождь", date="2024-06-01", time="14:30")
print(weather2)

weather3 = Weather(17, osadki="Туман")
print(weather3)
