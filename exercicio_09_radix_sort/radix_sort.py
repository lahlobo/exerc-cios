def counting_sort(arr, exp):
    """
    Função auxiliar para realizar o Counting Sort em um dígito específico.
    """
    n = len(arr)
    output = [0] * n  # Lista de saída
    count = [0] * 10  # Contagem para os dígitos (base 10)

    # Contagem de ocorrências
    for i in arr:
        index = (i // exp) % 10
        count[index] += 1

    # Atualizar a contagem para obter as posições reais
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Construir a lista ordenada
    i = n - 1
    while i >= 0:
        index = (arr[i] // exp) % 10
        output[count[index] - 1] = arr[i]
        count[index] -= 1
        i -= 1

    # Copiar para o arr original
    for i in range(n):
        arr[i] = output[i]


def radix_sort(arr):
    """
    Implementa o Radix Sort para números inteiros.
    """
    if len(arr) == 0:
        return arr

    # Encontrar o maior número para determinar o número de dígitos
    max_val = max(arr)

    # Aplicar o Counting Sort para cada dígito (base 10)
    exp = 1
    while max_val // exp > 0:
        counting_sort(arr, exp)
        exp *= 10


def radix_sort_binary(arr):
    """
    Implementa o Radix Sort usando a base 2.
    """
    if len(arr) == 0:
        return arr

    # Encontrar o maior número para determinar o número de bits
    max_val = max(arr)
    max_bits = max_val.bit_length()

    for bit in range(max_bits):
        # Separar os números com base no bit atual
        zero_bucket = []
        one_bucket = []
        for num in arr:
            if (num >> bit) & 1:
                one_bucket.append(num)
            else:
                zero_bucket.append(num)

        # Combinar os dois "baldes"
        arr[:] = zero_bucket + one_bucket


def test_radix_sort():
    print("Teste com Radix Sort em base 10:")
    nums = [170, 45, 75, 90, 802, 24, 2, 66]
    print(f"Lista original: {nums}")
    radix_sort(nums)
    print(f"Lista ordenada: {nums}\n")

    print("Teste com Radix Sort em base 2:")
    binary_nums = [170, 45, 75, 90, 802, 24, 2, 66]
    print(f"Lista original: {binary_nums}")
    radix_sort_binary(binary_nums)
    print(f"Lista ordenada: {binary_nums}")


if __name__ == "__main__":
    test_radix_sort()

