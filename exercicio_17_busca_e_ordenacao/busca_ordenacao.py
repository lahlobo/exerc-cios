# Função para realizar a busca Interpolation Search
def interpolation_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high and target >= arr[low] and target <= arr[high]:
        # Calculando a posição de busca com base na fórmula do Interpolation Search
        pos = low + ((target - arr[low]) * (high - low)) // (arr[high] - arr[low])
        
        # Verificando se encontramos o valor
        if arr[pos] == target:
            return pos
        if arr[pos] < target:
            low = pos + 1
        else:
            high = pos - 1
    return -1  # Caso o valor não seja encontrado

# Função para realizar o Bucket Sort
def bucket_sort(arr):
    # Número de baldes
    n = len(arr)
    
    # Criar baldes
    buckets = [[] for _ in range(n)]
    
    # Dividir os valores nas baldes
    for i in range(n):
        index = int(arr[i] * n // 101)  # Índice de cada balde baseado na nota
        buckets[index].append(arr[i])

    # Ordenar cada balde
    for i in range(n):
        buckets[i].sort()

    # Concatenar todos os baldes para formar a lista ordenada
    sorted_arr = []
    for bucket in buckets:
        sorted_arr.extend(bucket)
    
    return sorted_arr

# Lista de alunos e suas respectivas notas (entre 0 e 100)
students = [
    {'name': 'Ana', 'grade': 87},
    {'name': 'Carlos', 'grade': 92},
    {'name': 'Fernanda', 'grade': 78},
    {'name': 'Lucas', 'grade': 65},
    {'name': 'Mariana', 'grade': 85},
    {'name': 'Roberto', 'grade': 99},
    {'name': 'Paula', 'grade': 55},
    {'name': 'Pedro', 'grade': 72},
]

# Extraindo as notas dos alunos
grades = [student['grade'] for student in students]

# Ordenando as notas usando o Bucket Sort
sorted_grades = bucket_sort(grades)

# Exemplo de busca: Procurar um aluno com nota específica
target_grade = 92
result = interpolation_search(sorted_grades, target_grade)

# Verificando se a busca encontrou a nota
if result != -1:
    # Encontrando o aluno correspondente à nota
    for student in students:
        if student['grade'] == target_grade:
            print(f"Aluno encontrado: {student['name']} com a nota {student['grade']}")
else:
    print(f"Nota {target_grade} não encontrada.")
