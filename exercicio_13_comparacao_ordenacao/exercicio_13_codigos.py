import random
import time

# Funções de Ordenação
comparisons = 0

# Selection Sort
def selection_sort(arr):
    global comparisons
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            comparisons += 1
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

# Quick Sort
def quick_sort(arr):
    global comparisons
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    right = [x for x in arr if x > pivot]
    comparisons += len(arr) - 1
    return quick_sort(left) + [pivot] + quick_sort(right)

# Merge Sort
def merge_sort(arr):
    global comparisons
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    comparisons += len(arr) - 1
    return merge(left, right)

def merge(left, right):
    global comparisons
    result = []
    while left and right:
        comparisons += 1
        if left[0] < right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    result += left + right
    return result

# Função para testar e registrar os tempos
def test_sorting_algorithms():
    global comparisons
    results = []
    algorithms = {
        "Selection Sort": selection_sort,
        "Quick Sort": quick_sort,
        "Merge Sort": merge_sort,
        # Adicione os outros algoritmos aqui
    }

    for name, func in algorithms.items():
        comparisons = 0
        arr = [random.randint(0, 10000) for _ in range(1000)]  # Lista de teste
        start_time = time.time()
        func(arr.copy())
        elapsed_time = time.time() - start_time
        results.append((name, elapsed_time, comparisons))

    return results

# Exibindo resultados no terminal
for name, elapsed, comps in test_sorting_algorithms():
    print(f"{name}: {elapsed:.5f}s, {comps} comparações")
