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


if __name__ == "__main__":
    lista = [10, 20, 30, 40, 50]
    elemento = 30
    resultado = binary_search(lista, elemento)
    
    print(f"Lista: {lista}")
    print(f"Elemento procurado: {elemento}")
    print(f"Índice do elemento: {resultado}")
