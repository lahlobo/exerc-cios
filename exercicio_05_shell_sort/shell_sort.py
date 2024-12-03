def shell_sort(arr, sequence):
    """
    Implementa o Shell Sort com uma sequência de intervalos específica.
    """
    n = len(arr)
    gaps = sequence(n)
    for gap in gaps:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
    return arr

def shell_sequence(n):
    """Sequência de intervalos padrão de Shell."""
    gap = n // 2
    gaps = []
    while gap > 0:
        gaps.append(gap)
        gap //= 2
    return gaps

def knuth_sequence(n):
    """Sequência de intervalos de Knuth."""
    gaps = []
    gap = 1
    while gap < n:
        gaps.append(gap)
        gap = 3 * gap + 1
    return gaps[::-1]  # Reverso para começar com o maior gap

def hibbard_sequence(n):
    """Sequência de intervalos de Hibbard."""
    gaps = []
    k = 1
    while (gap := 2**k - 1) < n:
        gaps.append(gap)
        k += 1
    return gaps[::-1]  # Reverso para começar com o maior gap

def compare_shell_sort():
    """
    Compara o Shell Sort com diferentes sequências de intervalos.
    """
    import time
    import random

    sequences = {
        "Shell": shell_sequence,
        "Knuth": knuth_sequence,
        "Hibbard": hibbard_sequence
    }
    results = []

    # Listas de tamanhos variados
    test_cases = [random.sample(range(1, 10001), 1000), random.sample(range(1, 10001), 5000)]

    for test_id, test_case in enumerate(test_cases, start=1):
        print(f"Teste {test_id}:")
        for name, sequence in sequences.items():
            arr = test_case.copy()
            start_time = time.time()
            shell_sort(arr, sequence)
            duration = time.time() - start_time
            print(f"  {name} Sequence: {duration:.6f} segundos")
            results.append((name, len(test_case), duration))
        print("-" * 50)
    
    return results

if __name__ == "__main__":
    compare_shell_sort()
