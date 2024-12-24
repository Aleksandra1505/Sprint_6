import random
from datetime import datetime, timedelta

#набор имен
first_name = ["Саша", "Анна", "Андрей", "Дмитрий"]
#генерация случайного имени из списка
def generate_random_name():
    return random.choice(first_name )

#набор фамилий
last_name = ["Кац", "Капель", "Кот", "Бах"]
#генерация случайной фамилии из списка
def generate_random_last_name():
    return random.choice(last_name)

#генерация случайного адреса
def generate_address():
    streets = ["Новые черемушки", "Пирантелло", "Преображенская площадь", "Ленинский проспект"]
    house_number = random.randint(1, 150)
    apartment_number = random.randint(1, 500)
    city = random.choice(['Москва', 'Калуга', 'Липецк'])
    address = f"{random.choice(streets)}, дом {house_number}, кв. {apartment_number}, {city}"
    return address

#генерация случайного номера телефона
def generate_telephone_number():
    return f"+7{random.randint(1000000000, 9999999999)}"


#генерация случайной станции метро
def generate_random_metro_station():
    return random.randint(0, 224)

#генерация случайное количество дней от текущей даты в пределах 30 дней
def generate_random_date():
    random_days = random.randint(1, 30)
    random_date = datetime.now() + timedelta(days=random_days)
    return random_date.strftime('%d.%m.%Y')