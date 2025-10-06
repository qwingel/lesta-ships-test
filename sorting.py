# == Cортировка ==
#

# @func quick_sort(Iterable, None, None);
# Стандартная реализация быстрой сортировки
# @param arr - исходный массив/список чисел
# @param left - указатель на левый элемент, по умолчанию - None
# @param right - указатель на правый элемент, по умолчанию - None
# @return None
def quick_sort(arr, left = None, right = None):
    # Инициализируем указатели
    if left is None:
        left = 0
    if right is None:
        right = len(arr) - 1
    
    # Конец рекурсии
    if left >= right:
        return
    
    # Опорный элемент
    pivot = arr[(left + right) // 2]
    
    i = left
    j = right
    
    while i <= j:
        while arr[i] < pivot: i += 1
        while arr[j] > pivot: j -= 1
        
        if i <= j:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j -= 1
    
    if left < j:
        quick_sort(arr, left, j) # Рекурсия левой части
    
    if i < right:
        quick_sort(arr, i, right) # Рекурсия правой части


# Пример
if __name__ == "__main__":
    numbers = [64, 34, 25, 12, 22, 11, 90, 5]
    print("До сортировки:", numbers)
    
    quick_sort(numbers)
    print("После сортировки:", numbers)