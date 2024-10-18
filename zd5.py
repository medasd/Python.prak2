def tuple_stats(tpl):
    # Сумма всех элементов кортежа
    total_sum = sum(tpl)
    
    # Среднее значение элементов
    average = total_sum / len(tpl) if tpl else 0  # Обработка случая пустого кортежа
    
    # Кортеж с уникальными элементами
    unique_elements = tuple(set(tpl))
    
    return total_sum, average, unique_elements

# Запрос ввода от пользователя
input_numbers = input("Введите числа через запятую: ")

# Преобразование строки в кортеж чисел
try:
    numbers_tuple = tuple(map(int, input_numbers.split(',')))
    
    # Вызов функции и вывод результата
    result = tuple_stats(numbers_tuple)
    print(f"Результат: {result}")  # Вывод результата
except ValueError:
    print("Пожалуйста, введите только числа, разделенные запятыми.")
