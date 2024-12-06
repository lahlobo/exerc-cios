import matplotlib.pyplot as plt

# Função para mostrar o gráfico
def plot(arr, title):
    plt.figure(figsize=(10, 6))
    plt.bar(range(len(arr)), arr, color='skyblue')
    plt.title(title)
    plt.xlabel('Índice')
    plt.ylabel('Valor')
    plt.show()

# Função Merge Sort com visualização
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    # Mesclando as duas partes
    return merge(left, right, arr)

def merge(left, right, arr):
    i = j = k = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1
        plot(arr, f'Merge Sort - Passo: {arr}')
    
    # Se sobrar algum elemento de left ou right
    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1
        plot(arr, f'Merge Sort - Passo: {arr}')
    
    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1
        plot(arr, f'Merge Sort - Passo: {arr}')
    
    return arr

# Exemplo de uso
arr = [38, 27, 43, 3, 9, 82, 10]
merge_sort(arr)
////////////////////////////////////////////////////////

import matplotlib.pyplot as plt

# Função para mostrar o gráfico
def plot(arr, title):
    plt.figure(figsize=(10, 6))
    plt.bar(range(len(arr)), arr, color='lightgreen')
    plt.title(title)
    plt.xlabel('Índice')
    plt.ylabel('Valor')
    plt.show()

# Função Quick Sort com visualização
def quick_sort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
            plot(arr, f'Quick Sort - Passo: {arr}')
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    plot(arr, f'Quick Sort - Passo: {arr}')
    return i + 1

# Exemplo de uso
arr = [38, 27, 43, 3, 9, 82, 10]
quick_sort(arr, 0, len(arr) - 1)

//////////////////////////////////////////////////

import matplotlib.pyplot as plt

# Função para mostrar o gráfico
def plot(arr, title):
    plt.figure(figsize=(10, 6))
    plt.bar(range(len(arr)), arr, color='salmon')
    plt.title(title)
    plt.xlabel('Índice')
    plt.ylabel('Valor')
    plt.show()

# Função Selection Sort com visualização
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        plot(arr, f'Selection Sort - Passo: {arr}')

# Exemplo de uso
arr = [38, 27, 43, 3, 9, 82, 10]
selection_sort(arr)
