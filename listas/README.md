# Listas em Python 

## Listas

As listas são uma estrutura de dados que permite armazenar uma coleção de itens em ordem. Os itens podem ser de qualquer tipo, como números, strings, objetos, outras listas, etc.

Listas são estruturas de dados que podem armazenar vários valores. São mutáveis, ou seja, podemos alterar seus valores.

Em Python, as listas podem ser declaradas da seguinte forma: 

```python

lista = [1, 2, 3, 4, 5]

```




Veja que a lista acima armazena valores inteiros. Podemos armazenar qualquer tipo de dado em uma lista, inclusive outras listas. 

```python

lista = [1, 2, 3, 4, 5, [6, 7, 8]]

```

Podemos declarar um lista vazia em Python da seguinte forma:

```python

numeros = list()

```

ou ainda 

```python

numeros = []

```

As lista são comumente utilizadas em diversas aplicações no mundo real. Por exemplo, podemos armazenar os nomes de todos os alunos de uma turma em uma lista. 

```python

alunos = ["João", "Maria", "José", "Ana", "Pedro"]

```

As listas são mutáveis, o que significa que você pode adicionar, remover e alterar itens depois de criá-las. Exemplos:


```python

frutas = ["maçã", "banana", "laranja"]

# adicionar um item
frutas.append("manga")

# remover um item
frutas.remove("banana")

# alterar um item
frutas[1] = "kiwi"

```

## Acessando elementos de uma lista

Para acessar um elemento de uma lista, basta informar o índice do elemento desejado. 

```python

frutas = ["maçã", "banana", "laranja"]

# acessando o primeiro elemento da lista
frutas[0] # maçã

# acessando o segundo elemento da lista
frutas[1] # banana

# acessando o terceiro elemento da lista

frutas[2] # laranja

```

Você pode usar métodos e operadores para trabalhar com listas, como len() para obter o tamanho da lista, in para verificar se um item está na lista, + para concatenar listas, etc.

```python

frutas = ["maçã", "banana", "laranja"]

# tamanho da lista
len(frutas) # 3

# verificar se um item está na lista
"maçã" in frutas # True

# concatenar listas
frutas + ["manga"] # ["maçã", "banana", "laranja", "manga"]

```

## Iterando sobre uma lista

Você pode iterar sobre uma lista usando um laço for. 

```python

# percorrer a lista
for fruta in frutas:
    print(fruta)

# acessar um item
primeira_fruta = frutas[0]
```
