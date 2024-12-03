# Exercício 05: Shell Sort

Este exercício implementa o algoritmo Shell Sort com três diferentes sequências de intervalos: Shell, Knuth e Hibbard. Comparamos os tempos de execução em listas de diferentes tamanhos.

## Funcionamento
O Shell Sort utiliza sequências de intervalos para dividir a lista em sublistas menores e ordená-las progressivamente.

## Sequências Utilizadas
- **Shell**: `n/2, n/4, ..., 1`.
- **Knuth**: `3^k - 1`.
- **Hibbard**: `2^k - 1`.

## Como executar
Execute o arquivo `shell_sort.py` para rodar os testes comparativos.

## Observações
A escolha da sequência de intervalos afeta diretamente o desempenho do algoritmo. Sequências mais densas podem ser mais eficientes em listas muito grandes.
