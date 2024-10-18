# Создаем словарь со студентом
student = {
    'name': 'Madi',
    'age': 19,
    'grades': [90, 85, 78, 92, 88]
}

# Функция для вычисления средней оценки
def average_grade(student):
    grades = student['grades']
    return sum(grades) / len(grades)

# Запрос имени студента у пользователя
name_to_find = input("Введите имя студента: ")

# Проверка имени и вывод средней оценки
if name_to_find == student['name']:
    avg = average_grade(student)
    print(f"Средняя оценка студента {name_to_find}: {avg:.2f}")
else:
    print(f"Студент с именем {name_to_find} не найден.")
