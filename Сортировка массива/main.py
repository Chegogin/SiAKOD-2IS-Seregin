import random
import time

# Пузырьковая сортировка
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

# Быстрая сортировка
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

# Функция для тестирования производительности
def test_sorting_algorithms(size, num_tests=5):
    # Генерируем тестовый массив
    original_arr = [random.randint(1, 10000) for _ in range(size)]
    
    # Тестируем пузырьковую сортировку
    bubble_times = []
    for _ in range(num_tests):
        arr_copy = original_arr.copy()
        start_time = time.time()
        bubble_sort(arr_copy)
        end_time = time.time()
        bubble_times.append(end_time - start_time)
    
    # Тестируем быструю сортировку
    quick_times = []
    for _ in range(num_tests):
        arr_copy = original_arr.copy()
        start_time = time.time()
        quick_sort(arr_copy)
        end_time = time.time()
        quick_times.append(end_time - start_time)
    
    # Вычисляем среднее время
    avg_bubble = sum(bubble_times) / num_tests
    avg_quick = sum(quick_times) / num_tests
    
    return avg_bubble, avg_quick

# Тестирование на разных размерах массивов
sizes = [10, 100, 1000, 5000]
results = {}

for size in sizes:
    avg_bubble, avg_quick = test_sorting_algorithms(size)
    results[size] = (avg_bubble, avg_quick)
    
    print(f"\nРазмер массива: {size}")
    print(f"Пузырьковая сортировка: {avg_bubble:.6f} сек")
    print(f"Быстрая сортировка: {avg_quick:.6f} сек")
    print(f"Разница в скорости (Bubble/Quick): {avg_bubble/avg_quick:.2f}x")

# Пример сортировки небольшого массива
sample_arr = [64, 34, 25, 12, 22, 11, 90]
print("\nПример сортировки:")
print("Исходный массив:", sample_arr)
print("Bubble Sort:", bubble_sort(sample_arr.copy()))
print("Quick Sort:", quick_sort(sample_arr.copy()))