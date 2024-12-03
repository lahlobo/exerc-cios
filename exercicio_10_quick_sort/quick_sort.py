def quick_sort(arr, pivot_strategy="first"):
    """
    Implementa o Quick Sort com diferentes estratégias de escolha do pivô.
    :param arr: Lista a ser ordenada.
    :param pivot_strategy: Estratégia para escolher o pivô ("first", "last", "middle").
    :return: Lista ordenada.
    """
    if len(arr) <= 1:
        return arr

    # Escolha do pivô
    if pivot_strategy == "first":
        pivot = arr[0]
    elif pivot_strategy == "last":
        pivot = arr[-1]
    elif pivot_strategy == "middle":
        pivot = arr[len(arr) // 2]
    else:
        raise ValueError("Estratégia de pivô inválida. Use 'first', 'last' ou 'middle'.")

    # Particionar a lista
    less = [x for x in arr if x < pivot]
    equal = [x for x in arr if x == pivot]
    greater = [x for x in arr if x > pivot]

    # Ordenar recursivamente
    return quick_sort(less, pivot_strategy) + equal + quick_sort(greater, pivot_strategy)


def test_quick_sort():
    print("Teste do Quick Sort com diferentes estratégias de pivô:")

    test_cases = [
        ([10, 7, 8, 9, 1, 5], "Lista completamente desordenada"),
        ([1, 2, 3, 4, 5, 6], "Lista já ordenada"),
        ([6, 5, 4, 3, 2, 1], "Lista ordenada de forma decrescente")
    ]

    for arr, description in test_cases:
        print(f"\n{description}: {arr}")
        for strategy in ["first", "last", "middle"]:
            sorted_arr = quick_sort(arr, pivot_strategy=strategy)
            print(f"Pivô ({strategy}): {sorted_arr}")


if __name__ == "__main__":
    test_quick_sort()

