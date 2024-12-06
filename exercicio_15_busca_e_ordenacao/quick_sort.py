# Função para ordenar as palavras com Quick Sort
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

# Função de Binary Search para procurar uma palavra
def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid  # Palavra encontrada
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1  # Palavra não encontrada

# Exemplo de uso
words = ["banana", "apple", "cherry", "date"]
sorted_words = quick_sort(words)  # Ordenando as palavras
print("Palavras ordenadas:", sorted_words)

target_word = "date"
index = binary_search(sorted_words, target_word)
if index != -1:
    print(f"A palavra '{target_word}' foi encontrada na posição {index}.")
else:
    print(f"A palavra '{target_word}' não foi encontrada.")
