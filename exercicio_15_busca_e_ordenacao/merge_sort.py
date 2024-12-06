# Função para ordenar as palavras com Merge Sort
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)

# Função de merge para combinar duas listas ordenadas
def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result

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
sorted_words = merge_sort(words)  # Ordenando as palavras
print("Palavras ordenadas:", sorted_words)

target_word = "cherry"
index = binary_search(sorted_words, target_word)
if index != -1:
    print(f"A palavra '{target_word}' foi encontrada na posição {index}.")
else:
    print(f"A palavra '{target_word}' não foi encontrada.")
