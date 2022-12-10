# Manipulando matrizes com Python 

## Matrizes

Uma matriz é um array bidimensional, ou seja, uma tabela com linhas e colunas.

## Biblioteca Numpy

A biblioteca Numpy é uma biblioteca Python que permite realizar operações matemáticas em arrays multidimensionais.

Vamos importar a biblioteca Numpy e criar uma matriz com 3 linhas e 2 colunas.

```python
import numpy as np

x = np.empty((3, 2), dtype=np.int32)
```

A função empty() aloca memória para uma matriz de 3 linhas e 2 colunas do tipo inteiro.

### Acessando elementos de uma matriz

Vamos acessar o primeiro elemento da primeira linha da matriz.

```python
print(x[0][0])
```

### Alterando elementos de uma matriz

Vamos alterar o primeiro elemento da primeira linha da matriz.

```python
x[0][0] = 10
```

### Percorrendo uma matriz

Vamos percorrer a matriz e imprimir cada elemento.

```python
for i in range(len(x)):
    for j in range(len(x[i])):
        print(x[i][j])
```

### Matrizes com np.array()

Vamos criar uma matriz com 3 linhas e 2 colunas.

```python
x = np.array([[1, 2], [3, 4], [5, 6]])
```

### Matrizes com np.zeros()

Vamos criar uma matriz com 3 linhas e 2 colunas preenchidas com zeros.

```python
x = np.zeros((3, 2), dtype=np.int32)
```

### Matrizes com np.ones()

Vamos criar uma matriz com 3 linhas e 2 colunas preenchidas com uns.

```python
x = np.ones((3, 2), dtype=np.int32)
```

### Matrizes com np.full()

Vamos criar uma matriz com 3 linhas e 2 colunas preenchidas com o número 10.

```python
x = np.full((3, 2), 10, dtype=np.int32)
```

### Matrizes com np.eye()

Vamos criar uma matriz identidade 3x3.

```python
x = np.eye(3, dtype=np.int32)
```

### Matrizes com np.random.random()

Vamos criar uma matriz com 3 linhas e 2 colunas preenchidas com números aleatórios.

```python
x = np.random.random((3, 2))
```

### Matrizes com np.arange()

Vamos criar uma matriz com 3 linhas e 2 colunas preenchidas com números de 0 a 5.

```python
x = np.arange(6).reshape(3, 2)
```

### Matrizes com np.linspace()

Vamos criar uma matriz com 3 linhas e 2 colunas preenchidas com números de 0 a 5.

```python
x = np.linspace(0, 5, 6).reshape(3, 2)
```

### Matrizes com np.random.randint()

Vamos criar uma matriz com 3 linhas e 2 colunas preenchidas com números inteiros aleatórios de 0 a 10.

```python
x = np.random.randint(0, 10, 6).reshape(3, 2)
```

### Matrizes com np.random.normal()

Vamos criar uma matriz com 3 linhas e 2 colunas preenchidas com números aleatórios de uma distribuição normal.

```python
x = np.random.normal(0, 1, 6).reshape(3, 2)
```

