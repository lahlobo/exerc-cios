# Exercício 15: Busca e Ordenação em Strings

Este exercício aborda a adaptação dos algoritmos de ordenação **Merge Sort** e **Quick Sort** para ordenar palavras em ordem alfabética e a utilização do **Binary Search** para verificar se uma palavra específica está presente em uma lista de palavras ordenadas.

## Algoritmos Implementados

### 1. **Merge Sort**
O **Merge Sort** é um algoritmo de ordenação eficiente baseado na técnica de **dividir e conquistar**. Ele divide recursivamente a lista em duas metades, ordena essas metades e, em seguida, as combina.

### 2. **Quick Sort**
O **Quick Sort** é outro algoritmo de ordenação baseado em **dividir e conquistar**. Ele escolhe um "pivô" e reorganiza os elementos da lista para que todos os elementos menores que o pivô fiquem à esquerda, e os maiores à direita. O processo é repetido recursivamente nas duas metades.

### 3. **Binary Search**
O **Binary Search** é um algoritmo de busca eficiente que funciona apenas em listas ordenadas. Ele divide a lista ao meio, compara a chave de busca com o valor central e decide em qual metade buscar a chave.

## Como Funciona

1. **Ordenação com Merge Sort ou Quick Sort**: As palavras são ordenadas em ordem alfabética usando o **Merge Sort** ou o **Quick Sort**.
2. **Busca com Binary Search**: Após a ordenação, utilizamos o **Binary Search** para verificar se uma palavra específica está presente na lista ordenada.
