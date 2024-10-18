def tuple_stats(tpl):
    if not all(isinstance(i, (int, float)) for i in tpl):
        return "Ошибка: В кортеже должны быть только числа"
    
    total_sum = sum(tpl)
    avg_value = total_sum / len(tpl)
    unique_values = tuple(set(tpl))
    
    return total_sum, avg_value, unique_values

# Пример использования:
tpl = tuple(map(float, input("Введите числа через пробел для кортежа: ").split()))
print("Статистика по кортежу:", tuple_stats(tpl))
