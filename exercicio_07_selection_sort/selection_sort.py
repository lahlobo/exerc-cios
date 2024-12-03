def test_selection_sort():
    print("Teste com lista de números:")
    numbers = [64, 34, 25, 12, 22, 11, 90]
    print(f"Lista original: {numbers}\n")

    steps = selection_sort(numbers)

    print("Passo a passo da organização:")
    for i, step in enumerate(steps):
        print(f"Iteração {i + 1}: {step}")
    
    print(f"\nLista final ordenada: {numbers}")

if __name__ == "__main__":
    test_selection_sort()


/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

# Análise do desempenho: 

import time
import random

def analyze_selection_sort():
    sizes = [10, 100, 1000]  # Tamanhos das listas
    for size in sizes:
        test_list = random.sample(range(size * 10), size)  # Gera uma lista aleatória
        start_time = time.time()
        selection_sort(test_list)
        elapsed_time = time.time() - start_time
        print(f"Tempo para ordenar lista de tamanho {size}: {elapsed_time:.5f} segundos")

if __name__ == "__main__":
    analyze_selection_sort()

