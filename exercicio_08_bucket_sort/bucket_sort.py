def bucket_sort_floats(arr):
    """
    Implementa o Bucket Sort para números em ponto flutuante no intervalo [0, 1).
    """
    n = len(arr)
    if n == 0:
        return arr

    # Criar n baldes vazios
    buckets = [[] for _ in range(n)]

    # Distribuir os elementos nos baldes com base na posição
    for num in arr:
        index = int(num * n)
        buckets[index].append(num)

    # Ordenar os elementos de cada balde
    for i in range(n):
        buckets[i].sort()

    # Combinar todos os baldes
    sorted_array = []
    for bucket in buckets:
        sorted_array.extend(bucket)

    return sorted_array


def bucket_sort_integers(arr, bucket_size=10):
    """
    Adapta o Bucket Sort para ordenar números inteiros em intervalos maiores.
    """
    if len(arr) == 0:
        return arr

    # Encontrar valores máximo e mínimo
    min_val, max_val = min(arr), max(arr)

    # Calcular o número de baldes necessários
    bucket_count = (max_val - min_val) // bucket_size + 1
    buckets = [[] for _ in range(bucket_count)]

    # Distribuir os elementos nos baldes
    for num in arr:
        index = (num - min_val) // bucket_size
        buckets[index].append(num)

    # Ordenar os elementos de cada balde e combinar
    sorted_array = []
    for bucket in buckets:
        sorted_array.extend(sorted(bucket))

    return sorted_array


if __name__ == "__main__":
    # Testando números em ponto flutuante
    print("Teste com números em ponto flutuante no intervalo [0, 1):")
    float_nums = [0.78, 0.17, 0.39, 0.26, 0.72, 0.94, 0.21, 0.12, 0.23, 0.68]
    print(f"Lista original: {float_nums}")
    print(f"Lista ordenada: {bucket_sort_floats(float_nums)}\n")

    # Testando números inteiros
    print("Teste com números inteiros:")
    int_nums = [42, 32, 33, 52, 37, 47, 51]
    print(f"Lista original: {int_nums}")
    print(f"Lista ordenada: {bucket_sort_integers(int_nums, bucket_size=10)}")
