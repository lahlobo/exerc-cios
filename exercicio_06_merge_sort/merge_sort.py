def merge_sort_numbers(arr):
    """
    Implementa o Merge Sort para ordenar uma lista de números inteiros.
    """
    if len(arr) > 1:
        # Divisão da lista
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        # Chamada recursiva
        merge_sort_numbers(left_half)
        merge_sort_numbers(right_half)

        # Mesclagem
        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1
////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

def merge_sort_strings(arr):
    """
    Implementa o Merge Sort para ordenar uma lista de strings em ordem alfabética.
    """
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort_strings(left_half)
        merge_sort_strings(right_half)

        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i].lower() < right_half[j].lower():
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1


