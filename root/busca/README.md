# Algoritmos de Busca 

Os algoritmos de busca são algoritmos que tem como objetivo encontrar um elemento em uma lista ou em outra estrutura de dados.

Existem diversos algoritmos de busca, cada um com sua particularidade. Neste capítulo, iremos estudar alguns dos algoritmos mais comuns.

## Busca Sequencial

A busca sequencial é um algoritmo de busca que percorre a lista de elementos até encontrar o elemento desejado. Caso o elemento não seja encontrado, o algoritmo retorna um valor especial, como -1.

```python

def busca_sequencial(lista, elemento):
    for i in range(len(lista)):
        if lista[i] == elemento:
            return i
    return -1

```

## Busca Binária

A busca binária é um algoritmo de busca que funciona apenas em listas ordenadas. O algoritmo funciona da seguinte forma:

1. Encontra o elemento do meio da lista
2. Compara o elemento do meio com o elemento desejado
3. Se o elemento do meio for igual ao elemento desejado, retorna o índice do elemento do meio
4. Se o elemento do meio for menor que o elemento desejado, repete o processo na metade da lista à direita do elemento do meio
5. Se o elemento do meio for maior que o elemento desejado, repete o processo na metade da lista à esquerda do elemento do meio
6. Se o elemento não for encontrado, retorna um valor especial, como -1

```python

def busca_binaria(lista, elemento):
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

```

## Busca Interpolação

A busca por interpolação é um algoritmo de busca que funciona apenas em listas ordenadas. O algoritmo funciona da seguinte forma:

1. Encontra o elemento de acordo com a fórmula: `posicao = inicio + ((fim - inicio) // (lista[fim] - lista[inicio])) * (elemento - lista[inicio])`
2. Compara o elemento encontrado com o elemento desejado
3. Se o elemento encontrado for igual ao elemento desejado, retorna o índice do elemento encontrado
4. Se o elemento encontrado for menor que o elemento desejado, repete o processo na metade da lista à direita do elemento encontrado
5. Se o elemento encontrado for maior que o elemento desejado, repete o processo na metade da lista à esquerda do elemento encontrado

```python

def busca_interpolacao(lista, elemento):
    inicio = 0
    fim = len(lista) - 1

    while inicio <= fim:
        posicao = inicio + ((fim - inicio) // (lista[fim] - lista[inicio])) * (elemento - lista[inicio])
        if lista[posicao] == elemento:
            return posicao
        elif lista[posicao] < elemento:
            inicio = posicao + 1
        else:
            fim = posicao - 1
    return -1

```

A busca por interpolação é mais eficiente que a busca binária, porém, é necessário que a lista esteja ordenada. Caso a lista não esteja ordenada, a busca por interpolação pode retornar um índice inválido.


