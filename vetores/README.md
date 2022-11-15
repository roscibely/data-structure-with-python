# Vetores em Python 

## O que é um vetor?

Um vetor é uma estrutura de dados que armazena um conjunto de valores do mesmo tipo.

## Vetores em Python

Em Python, um vetor é representado por uma lista. 

```python
x = [1, 2, 3, 4, 5]
```

## Biblioteca Numpy

A biblioteca Numpy é uma biblioteca Python que permite realizar operações matemáticas em arrays multidimensionais.

Vamos importar a biblioteca Numpy e criar um vetor com 5 elementos.

```python
import numpy as np

x = np.empty(5, dtype=np.int32)
```

A função empty() aloca memória para um vetor de 5 elementos do tipo inteiro.

### Acessando elementos de um vetor

Vamos acessar o primeiro elemento do vetor.

```python
print(x[0])
```

### Alterando elementos de um vetor

Vamos alterar o primeiro elemento do vetor.

```python
x[0] = 10
```

### Percorrendo um vetor

Vamos percorrer o vetor e imprimir cada elemento.

```python
for i in range(len(x)):
    print(x[i])
```

### Vetores com np.array()

Vamos criar um vetor com 5 elementos.

```python
x = np.array([1, 2, 3, 4, 5])
```

### Vetores com np.zeros()

Vamos criar um vetor com 5 elementos preenchidos com zeros.

```python
x = np.zeros(5, dtype=np.int32)
```

### Vetores com np.ones()

Vamos criar um vetor com 5 elementos preenchidos com uns.

```python
x = np.ones(5, dtype=np.int32)
```

### Vetores com np.full()

Vamos criar um vetor com 5 elementos preenchidos com o número 10.

```python
x = np.full(5, 10, dtype=np.int32)
```

### Vetores com np.arange()

Vamos criar um vetor com 5 elementos preenchidos com os números de 0 a 4.

```python
x = np.arange(5)
```

### Vetores com np.linspace()

Vamos criar um vetor com 5 elementos preenchidos com os números de 0 a 4.

```python
x = np.linspace(0, 4, 5)
```

### Vetores com np.random.randint()

Vamos criar um vetor com 5 elementos preenchidos com números aleatórios entre 0 e 10.

```python
x = np.random.randint(0, 10, 5)
```

### Vetores de strings

Vamos criar um vetor com 5 elementos do tipo string.

```python
x = np.array(['a', 'b', 'c', 'd', 'e'])
```

### Vetores de booleanos


Vamos criar um vetor com 5 elementos do tipo booleano.

```python
x = np.array([True, False, True, False, True])
```

### Vetores com np.random.choice()

Vamos criar um vetor com 5 elementos preenchidos com números aleatórios entre 0 e 10.

```python
x = np.random.choice(10, 5)
```

