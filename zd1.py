def analyze_list(lst):
    if not all(isinstance(i, (int, float)) for i in lst):
        raise ValueError("Все элементы списка должны быть числами.")
    if len(lst) == 0:
        raise ValueError("Список не должен быть пустым.")
    
    lst_sorted = sorted(lst)
    max_val = max(lst)
    min_val = min(lst)
    avg_val = sum(lst) / len(lst)
    med_val = lst_sorted[len(lst) // 2] if len(lst) % 2 != 0 else (lst_sorted[len(lst) // 2 - 1] + lst_sorted[len(lst) // 2]) / 2

    return {
        'max': max_val,
        'min': min_val,
        'avg': avg_val,
        'med': med_val
    }

lst_input = list(map(float, input("Введите список чисел через пробел: ").split()))
print(analyze_list(lst_input))
