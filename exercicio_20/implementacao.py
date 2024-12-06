import random
import time

# Algoritmos de Ordenação
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

# Algoritmos de Busca
def linear_search(arr, target):
    for i, value in enumerate(arr):
        if value == target:
            return i
    return -1

def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

# Função para medir o tempo de execução
def measure_time(func, *args):
    start_time = time.time()
    result = func(*args)
    end_time = time.time()
    return result, end_time - start_time

# Função principal
def main():
    # Gerar uma lista aleatória
    lista = [random.randint(0, 1000) for _ in range(1000)]
    
    print("Escolha um algoritmo de ordenação:")
    print("1. Bubble Sort")
    print("2. Selection Sort")
    print("3. Merge Sort")
    ordenacao_choice = int(input("Digite o número do algoritmo escolhido: "))
    
    if ordenacao_choice == 1:
        sort_func = bubble_sort
    elif ordenacao_choice == 2:
        sort_func = selection_sort
    elif ordenacao_choice == 3:
        sort_func = merge_sort
    else:
        print("Escolha inválida.")
        return

    # Ordenação
    print("\nOrdenando a lista...")
    sorted_list, sort_time = measure_time(sort_func, lista)
    print(f"Lista ordenada: {sorted_list[:10]}...")  # Exibe os primeiros 10 elementos
    print(f"Tempo de execução da ordenação: {sort_time:.6f} segundos\n")

    print("Escolha um algoritmo de busca:")
    print("1. Busca Linear")
    print("2. Busca Binária")
    busca_choice = int(input("Digite o número do algoritmo escolhido: "))
    
    target = random.choice(sorted_list)  # Escolher um valor aleatório da lista ordenada

    if busca_choice == 1:
        search_func = linear_search
    elif busca_choice == 2:
        search_func = binary_search
    else:
        print("Escolha inválida.")
        return
    
    # Busca
    print(f"\nBuscando o valor {target}...")
    search_result, search_time = measure_time(search_func, sorted_list, target)
    if search_result != -1:
        print(f"Elemento encontrado na posição {search_result}")
    else:
        print("Elemento não encontrado.")
    print(f"Tempo de execução da busca: {search_time:.6f} segundos")

if __name__ == "__main__":
    main()
