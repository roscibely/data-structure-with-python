# Alocação dinâmica em Python 

Alocação dinâmica é um conceito que se aplica a qualquer linguagem de programação. 

A alocação dinâmica de memória não é um problema em Python. Isso porque a linguagem é interpretável e não compilável. O gerenciador de memória Python gerencia a alocação ou desalocação do espaço de memória por meio das funções da API.



## O que é alocação dinâmica?

Alocação dinâmica é o processo de alocar memória em tempo de execução. Em outras palavras, é o processo de criar variáveis em tempo de execução. 

Na linguagem python não realizamos alocação dinâmica explicitamente. A alocação é feita automaticamente quando criamos uma variável.

```python
x = 10 # x é uma variável inteira
```

## Alocação com Cython 

A biblioteca Cython é uma extensão do Python que permite escrever código em C e C ++ dentro do Python para entender melhor o que é alocação dinâmica. 

Vamos importar a biblioteca Cython e criar uma função que aloca memória para um inteiro.

```python
from cython cimport malloc, free

cdef int *x = <int *> malloc(sizeof(int))
```

A função malloc() aloca memória para um inteiro. A função free() libera a memória alocada. 

```python
free(x)
```

## Alocação com ctypes

A biblioteca ctypes é uma biblioteca Python que permite chamar funções em bibliotecas dinâmicas C.

Vamos importar a biblioteca ctypes e criar uma função que aloca memória para um inteiro.

```python
from ctypes import *

c_int_p = POINTER(c_int)

x = c_int_p()
```

A função POINTER() aloca memória para um inteiro. A função free() libera a memória alocada. 

```python
free(x)
```

## Alocação com Numpy

A biblioteca Numpy é uma biblioteca Python que permite realizar operações matemáticas em arrays multidimensionais.

Vamos importar a biblioteca Numpy e criar uma função que aloca memória para um inteiro.

```python
import numpy as np

x = np.empty(1, dtype=np.int32)
```

A função empty() aloca memória para um inteiro. 













