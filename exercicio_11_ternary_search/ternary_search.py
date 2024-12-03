# Implementação do Binary Search
def binary_search(arr, target):
    """
    Implementa o algoritmo Binary Search.
    :param arr: Lista ordenada.
    :param target: Elemento a ser encontrado.
    :return: Índice do elemento ou -1 se não encontrado.
    """
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

# Implementação do Ternary Search
def ternary_search(arr, left, right, target):
    """
    Implementa o algoritmo Ternary Search.
    :param arr: Lista ordenada.
    :param left: Índice da parte inicial da lista.
    :param right: Índice da parte final da lista.
    :param target: Elemento a ser encontrado.
    :return: Índice do elemento ou -1 se não encontrado.
    """
    if right >= left:
        # Calculando os dois pontos de divisão
        mid1 = left + (right - left) // 3
        mid2 = right - (right - left) // 3

        # Verificando as três partes
        if arr[mid1] == target:
            return mid1
        elif arr[mid2] == target:
            return mid2
        elif target < arr[mid1]:
            return ternary_search(arr, left, mid1 - 1, target)
        elif target > arr[mid2]:
            return ternary_search(arr, mid2 + 1, right, target)
        else:
            return ternary_search(arr, mid1 + 1, mid2 - 1, target)

    return -1  # Retorna -1 se o elemento não for encontrado

# Função para testar ambos os algoritmos
def test_search_comparison():
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    
    # Testando o Binary Search
    target = 7
    binary_result = binary_search(arr, target)
    print(f"Binary Search: Elemento {target} encontrado no índice: {binary_result}")
    
    # Testando o Ternary Search
    ternary_result = ternary_search(arr, 0, len(arr) - 1, target)
    print(f"Ternary Search: Elemento {target} encontrado no índice: {ternary_result}")
    
    # Testando para um número que não existe
    target = 11
    binary_result = binary_search(arr, target)
    print(f"Binary Search: Elemento {target} encontrado no índice: {binary_result}")
    
    ternary_result = ternary_search(arr, 0, len(arr) - 1, target)
    print(f"Ternary Search: Elemento {target} encontrado no índice: {ternary_result}")

if __name__ == "__main__":
    test_search_comparison()
