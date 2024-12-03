import math

def jump_search(lista, elemento):
    """
    Implementação do algoritmo Jump Search.
    Retorna o índice do elemento ou -1 se não encontrado.
    """
    n = len(lista)
    salto = int(math.sqrt(n))  # Tamanho do salto ideal

    inicio = 0
    fim = min(salto, n)

    # "Salta" entre os blocos até encontrar um bloco onde o elemento pode estar
    while fim < n and lista[fim] < elemento:
        inicio = fim
        fim += salto
        if fim > n - 1:
            fim = n

    # Realiza uma busca linear dentro do bloco
    for i in range(inicio, fim):
        if lista[i] == elemento:
            return i

    return -1

def realizar_testes():
    """
    Realiza testes comparativos entre o Jump Search e o Binary Search.
    """
    from time import time

    def binary_search(lista, elemento):
        inicio = 0
        fim = len(lista) - 1

        while inicio <= fim:
            meio = (inicio + fim) // 2
            if lista[meio] == elemento:
                return meio
            if lista[meio] < elemento:
                inicio = meio + 1
            else:
                fim = meio - 1
        return -1

    # Casos de teste
    testes = [
        {"lista": list(range(1, 10001)), "elemento": 5000, "descricao": "Lista uniforme grande"},
        {"lista": [1, 3, 7, 15, 31, 63, 127, 255, 511], "elemento": 127, "descricao": "Lista não uniforme"},
        {"lista": [1, 5, 10, 20, 40, 80, 160], "elemento": 40, "descricao": "Lista não uniforme menor"},
        {"lista": [1, 2, 3, 4, 5], "elemento": 6, "descricao": "Elemento não existente"}
    ]

    for i, teste in enumerate(testes):
        lista = teste["lista"]
        elemento = teste["elemento"]
        descricao = teste["descricao"]

        # Medir tempo do Jump Search
        inicio_tempo = time()
        resultado_jump = jump_search(lista, elemento)
        tempo_jump = time() - inicio_tempo

        # Medir tempo do Binary Search
        inicio_tempo = time()
        resultado_bin = binary_search(lista, elemento)
        tempo_bin = time() - inicio_tempo

        # Exibir resultados
        print(f"Teste {i + 1}: {descricao}")
        print(f"  Lista: {lista}")
        print(f"  Elemento procurado: {elemento}")
        print(f"  Resultado Jump Search: {resultado_jump}, Tempo: {tempo_jump:.6f} segundos")
        print(f"  Resultado Binary Search: {resultado_bin}, Tempo: {tempo_bin:.6f} segundos")
        print("  Observação: ", " Mais rápido" if tempo_jump < tempo_bin else " Mais lento")
        print("-" * 50)


if __name__ == "__main__":
    realizar_testes()
