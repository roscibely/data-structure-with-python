# Algoritmos de Ordenação 

Os algoritmos de ordenação são algoritmos que tem como objetivo ordenar um conjunto de dados. Em situações práticas, tais como, busca de dados em um banco de dados, é necessário que os dados estejam ordenados para que a busca seja feita de forma eficiente.

No mundo real, os algoritmos de ordenação são utilizados para ordenar dados de forma crescente ou decrescente. Por exemplo, uma lista de nomes, um conjunto de números, etc.

## Tipos de Ordenação

Existem diversos tipos de ordenação, porém, os mais comuns são:

- Ordenação por Intercalação
- Ordenação por Seleção
- Ordenação por Inserção
- Ordenação por Troca
- Ordenação por Contagem
- Ordenação por Distribuição

## Ordenação por Intercalação

A ordenação por intercalação é um algoritmo de ordenação que consiste em dividir o conjunto de dados em duas partes, ordenar cada uma das partes e depois intercalar as duas partes ordenadas.

Exemplo de implementação com Python:

```python

# implementação recursiva
def merge_sort(lista):
    if len(lista) <= 1:
        return lista

    meio = len(lista) // 2
    lado_esquerdo = merge_sort(lista[:meio])
    lado_direito = merge_sort(lista[meio:])

    return merge(lado_esquerdo, lado_direito)

# implementação da função merge
def merge(lado_esquerdo, lado_direito):
    if not lado_esquerdo:
        return lado_direito

    if not lado_direito:
        return lado_esquerdo

    if lado_esquerdo[0] < lado_direito[0]:
        return [lado_esquerdo[0]] + merge(lado_esquerdo[1:], lado_direito)

    return [lado_direito[0]] + merge(lado_esquerdo, lado_direito[1:])

```


## Ordenação por Seleção

A ordenação por seleção é um algoritmo de ordenação que consiste em percorrer o conjunto de dados e selecionar o menor elemento, trocando-o com o elemento da primeira posição. Em seguida, percorre o conjunto de dados novamente, selecionando o menor elemento e trocando-o com o elemento da segunda posição. O processo é repetido até que todos os elementos estejam ordenados.

Exemplo de implementação com Python:

```python

def selection_sort(lista):
    fim = len(lista)

    for i in range(fim - 1):
        # inicialmente, o menor elemento já visto é o i-ésimo
        posicao_do_minimo = i

        for j in range(i + 1, fim):
            if lista[j] < lista[posicao_do_minimo]:
                posicao_do_minimo = j

        # Coloca o menor elemento encontrado no início da sub-lista
        # para ordenar os elementos até a posição i
        lista[i], lista[posicao_do_minimo] = lista[posicao_do_minimo], lista[i]

```

## Ordenação por Inserção

A ordenação por inserção é um algoritmo de ordenação que consiste em percorrer o conjunto de dados e inserir cada elemento na posição correta. Para isso, é necessário percorrer a lista até o elemento anterior ao elemento que está sendo inserido e verificar se o elemento que está sendo inserido é menor que o elemento anterior. Caso seja, o elemento anterior é deslocado para a direita e o elemento que está sendo inserido é inserido na posição anterior.

Exemplo de implementação com Python:

```python

def insertion_sort(lista):
    for i in range(1, len(lista)):
        chave = lista[i]
        j = i - 1
        while j >= 0 and chave < lista[j]:
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = chave

```

## Ordenação por Troca

A ordenação por troca é um algoritmo de ordenação que consiste em percorrer o conjunto de dados e trocar dois elementos de posição se o primeiro elemento for maior que o segundo elemento. O processo é repetido até que todos os elementos estejam ordenados.

Exemplo de implementação com Python:

```python

def bubble_sort(lista):
    fim = len(lista)

    for i in range(fim - 1, 0, -1):
        for j in range(i):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]

```




