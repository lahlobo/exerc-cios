def interpolation_search(lista, elemento):
    """
    Implementação do algoritmo de busca por interpolação.
    Retorna o índice do elemento na lista ou -1 se não for encontrado.
    """
    inicio = 0
    fim = len(lista) - 1

    while inicio <= fim and lista[inicio] <= elemento <= lista[fim]:
        # Fórmula para calcular a posição
        pos = inicio + ((fim - inicio) * (elemento - lista[inicio]) // (lista[fim] - lista[inicio]))

        # Verifica se o elemento foi encontrado
        if lista[pos] == elemento:
            return pos

        # Ajusta os limites para a próxima iteração
        if lista[pos] < elemento:
            inicio = pos + 1
        else:
            fim = pos - 1

    return -1


def realizar_testes():
    """
    Realiza testes comparativos entre o Interpolation Search e o Binary Search.
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
        {"lista": list(range(1, 1001)), "elemento": 500, "descricao": "Lista uniforme grande"},
        {"lista": [1, 3, 7, 15, 31, 63, 127, 255, 511], "elemento": 127, "descricao": "Lista não uniforme"},
        {"lista": [1, 5, 10, 20, 40, 80, 160], "elemento": 40, "descricao": "Lista não uniforme menor"},
        {"lista": [1, 2, 3, 4, 5], "elemento": 6, "descricao": "Elemento não existente"}
    ]

    for i, teste in enumerate(testes):
        lista = teste["lista"]
        elemento = teste["elemento"]
        descricao = teste["descricao"]

        # Medir tempo do Interpolation Search
        inicio_tempo = time()
        resultado_interp = interpolation_search(lista, elemento)
        tempo_interp = time() - inicio_tempo

        # Medir tempo do Binary Search
        inicio_tempo = time()
        resultado_bin = binary_search(lista, elemento)
        tempo_bin = time() - inicio_tempo

        # Exibir resultados
        print(f"Teste {i + 1}: {descricao}")
        print(f"  Lista: {lista}")
        print(f"  Elemento procurado: {elemento}")
        print(f"  Resultado Interpolation Search: {resultado_interp}, Tempo: {tempo_interp:.6f} segundos")
        print(f"  Resultado Binary Search: {resultado_bin}, Tempo: {tempo_bin:.6f} segundos")
        print("  Observação: ", "✔️ Mais rápido" if tempo_interp < tempo_bin else "❌ Mais lento")
        print("-" * 50)


if __name__ == "__main__":
    realizar_testes()
