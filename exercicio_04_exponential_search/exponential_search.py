def binary_search(arr, low, high, x):
    """Função de busca binária."""
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            low = mid + 1
        else:
            high = mid - 1
    return -1

def exponential_search(arr, x):
    """Implementação do algoritmo Exponential Search."""
    n = len(arr)
    
    # Se o elemento no primeiro índice for o procurado
    if arr[0] == x:
        return 0
    
    # Encontre o intervalo em que o elemento pode estar
    i = 1
    while i < n and arr[i] <= x:
        i *= 2

    # Faça uma busca binária dentro do intervalo encontrado
    return binary_search(arr, i // 2, min(i, n-1), x)

def realizar_testes():
    """
    Realiza testes comparativos entre o Exponential Search e o Binary Search.
    """
    from time import time

    def binary_search(arr, low, high, x):
        while low <= high:
            mid = (low + high) // 2
            if arr[mid] == x:
                return mid
            elif arr[mid] < x:
                low = mid + 1
            else:
                high = mid - 1
        return -1

    # Casos de teste
    testes = [
        {"lista": list(range(1, 10001)), "elemento": 5000, "descricao": "Lista grande uniforme"},
        {"lista": [1, 3, 7, 15, 31, 63, 127, 255, 511], "elemento": 127, "descricao": "Lista não uniforme"},
        {"lista": [1, 5, 10, 20, 40, 80, 160], "elemento": 40, "descricao": "Lista não uniforme pequena"},
        {"lista": [1, 2, 3, 4, 5], "elemento": 6, "descricao": "Elemento não existente"}
    ]

    for i, teste in enumerate(testes):
        lista = teste["lista"]
        elemento = teste["elemento"]
        descricao = teste["descricao"]

        # Medir tempo do Exponential Search
        inicio_tempo = time()
        resultado_exp = exponential_search(lista, elemento)
        tempo_exp = time() - inicio_tempo

        # Medir tempo do Binary Search
        inicio_tempo = time()
        resultado_bin = binary_search(lista, 0, len(lista)-1, elemento)
        tempo_bin = time() - inicio_tempo

        # Exibir resultados
        print(f"Teste {i + 1}: {descricao}")
        print(f"  Lista: {lista}")
        print(f"  Elemento procurado: {elemento}")
        print(f"  Resultado Exponential Search: {resultado_exp}, Tempo: {tempo_exp:.6f} segundos")
        print(f"  Resultado Binary Search: {resultado_bin}, Tempo: {tempo_bin:.6f} segundos")
        print("  Observação: ", " Mais rápido" if tempo_exp < tempo_bin else " Mais lento")
        print("-" * 50)

if __name__ == "__main__":
    realizar_testes()
