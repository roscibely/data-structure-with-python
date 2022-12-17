# Complexidade de Algoritmos 

## O que é complexidade de algoritmos?

Complexidade de algoritmos é uma medida de desempenho de um algoritmo. É uma medida de tempo e espaço de memória que um algoritmo consome para executar uma tarefa.

## Como medir a complexidade de algoritmos?

Existem duas formas de medir a complexidade de algoritmos:

- Tempo de execução
- Espaço de memória

### Tempo de execução

O tempo de execução de um algoritmo é a quantidade de tempo que o algoritmo leva para executar uma tarefa. Para medir o tempo de execução de um algoritmo, é necessário executar o algoritmo com diferentes entradas e calcular o tempo de execução para cada entrada. O tempo de execução de um algoritmo é a soma dos tempos de execução para cada entrada.

### Espaço de memória

O espaço de memória de um algoritmo é a quantidade de memória que o algoritmo consome para executar uma tarefa. Para medir o espaço de memória de um algoritmo, é necessário executar o algoritmo com diferentes entradas e calcular o espaço de memória para cada entrada. O espaço de memória de um algoritmo é a soma dos espaços de memória para cada entrada.

## Como calcular a complexidade de algoritmos?

Existem duas formas de calcular a complexidade de algoritmos:

- Complexidade de tempo

- Complexidade de espaço

### Complexidade de tempo

A complexidade de tempo de um algoritmo é denotada por T(n), em que n é o tamanho da entrada. A complexidade de tempo de um algoritmo é a quantidade de tempo que o algoritmo leva para executar uma tarefa com uma entrada de tamanho n. 

Normalmente, utilizamos a notação big-O para denotar a complexidade de tempo de um algoritmo. A notação big-O denota o limite superior da complexidade de tempo de um algoritmo. 

Por exemplo, se T(n) = 2n + 1, então T(n) = O(n).

### Complexidade de espaço

A complexidade de espaço de um algoritmo é denotada por S(n), em que n é o tamanho da entrada. A complexidade de espaço de um algoritmo é a quantidade de memória que o algoritmo consome para executar uma tarefa com uma entrada de tamanho n.

Normalmente, utilizamos a notação big-O para denotar a complexidade de espaço de um algoritmo. A notação big-O denota o limite superior da complexidade de espaço de um algoritmo. 


### Exemplo de complexidade de tempo: 

```python
# complexidade.py

def soma(n):
    resultado = 0
    for i in range(n):
        resultado += i
    return resultado

print(soma(10))
```

O código acima calcula a soma dos números de 0 a n-1. Para calcular a soma dos números de 0 a n-1, o algoritmo soma os números de 0 a n-1. Para cada número de 0 a n-1, o algoritmo soma o número atual com o resultado. O algoritmo faz isso n vezes, uma vez para cada número de 0 a n-1. Portanto, o algoritmo leva n vezes para calcular a soma dos números de 0 a n-1.

A complexidade de tempo de soma(n) é denotada por T(n). T(n) = O(n), pois o algoritmo leva n vezes para calcular a soma dos números de 0 a n-1.

### Exemplo de complexidade de espaço: 

```python
# complexidade.py

def soma(n):
    resultado = 0
    for i in range(n):
        resultado += i
    return resultado

print(soma(10))

```

A complexidade de espaço de soma(n) é denotada por S(n). S(n) = O(1), pois o algoritmo consome uma quantidade constante de memória para calcular a soma dos números de 0 a n-1.

## Exercícios

1. Considere o seguinte algoritmo que realiza a multiplicação de matrizes:

```python
# multiplicacao.py

def multiplicacao(A, B):
    C = []
    for i in range(len(A)):
        C.append([])
        for j in range(len(B[0])):
            C[i].append(0)
            for k in range(len(B)):
                C[i][j] += A[i][k] * B[k][j]
    return C

A = [[1, 2], [3, 4]]
B = [[5, 6], [7, 8]]
print(multiplicacao(A, B))
```

a) Qual é a complexidade de tempo de multiplicacao(A, B)?

b) Qual é a complexidade de espaço de multiplicacao(A, B)?

2. Considere o seguinte algoritmo que realiza a busca binária em uma lista ordenada:

```python
# busca.py

def busca(lista, elemento):
    inicio = 0
    fim = len(lista) - 1
    while inicio <= fim:
        meio = (inicio + fim) // 2
        if lista[meio] == elemento:
            return meio
        elif lista[meio] < elemento:
            inicio = meio + 1
        else:
            fim = meio - 1
    return -1

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(busca(lista, 5))
```

a) Qual é a complexidade de tempo de busca(lista, elemento)?

b) Qual é a complexidade de espaço de busca(lista, elemento)?

Respostas:

1. a) T(n) = O(n^3)

b) S(n) = O(n^2)

2. a) T(n) = O(log n)

b) S(n) = O(1)





