# Função para ordenar a lista de livros com base no ISBN
def binary_search(books, target_isbn):
    low = 0
    high = len(books) - 1

    while low <= high:
        mid = (low + high) // 2
        # Comparar o ISBN no meio da lista com o ISBN de busca
        if books[mid]['ISBN'] == target_isbn:
            return mid  # Livro encontrado
        elif books[mid]['ISBN'] < target_isbn:
            low = mid + 1
        else:
            high = mid - 1
    return -1  # Livro não encontrado

# Exemplo de lista de livros, ordenada por ISBN
books = [
    {'ISBN': '978-3-16-148410-0', 'title': 'Python Programming', 'author': 'John Doe'},
    {'ISBN': '978-1-23-456789-7', 'title': 'Data Science Fundamentals', 'author': 'Jane Smith'},
    {'ISBN': '978-0-12-345678-9', 'title': 'Machine Learning Basics', 'author': 'Alice Johnson'},
    {'ISBN': '978-0-13-110362-7', 'title': 'Introduction to Algorithms', 'author': 'Thomas Cormen'},
    {'ISBN': '978-0-07-352332-2', 'title': 'The Art of Computer Programming', 'author': 'Donald Knuth'}
]

# Ordenando a lista de livros por ISBN (isso seria feito antes da busca binária)
books = sorted(books, key=lambda x: x['ISBN'])

# Exemplo de busca binária
target_isbn = '978-0-13-110362-7'
index = binary_search(books, target_isbn)

# Exibindo o resultado
if index != -1:
    book = books[index]
    print(f"Livro encontrado: {book['title']} por {book['author']} (ISBN: {book['ISBN']})")
else:
    print(f"Livro com ISBN {target_isbn} não encontrado.")
