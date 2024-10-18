
phonebook = {
    '+123456789': 'Madi',
    '+987654321': 'Nazarbaev',
    '+555123456': 'Palmer',
    '+777888999': 'Sanjar'
}

# Функция для поиска номера телефона по имени
def reverse_lookup(name, phonebook):
    for phone, person in phonebook.items():
        if person == name:
            return phone
    return "Имя не найдено"

# Запрос имени у пользователя
name_to_find = input("Введите имя: ")

# Поиск номера телефона
phone = reverse_lookup(name_to_find, phonebook)

# Вывод результата
print(f"Номер телефона для {name_to_find}: {phone}")
