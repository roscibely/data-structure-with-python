# Variáveis em Python 

As variáveis são espaços na memória do computador que armazenam valores.

## Declaração de variáveis

Em Python, a declaração de variáveis é feita de forma implícita, ou seja, não é necessário declarar o tipo da variável.

### Exemplo 1

```python
>>> x = 5
>>> y = "Hello, World!"
>>> print(x)
5
>>> print(y)
Hello, World!
```

### Exemplo 2

```python
>>> x = 4       # x é do tipo int
>>> x = "Sally" # x é do tipo str
>>> print(x)
Sally
```

## Tipos de variáveis em Python 

### Tipos numéricos

Os tipos numéricos em Python são `int`, `float` e `complex`.

#### Exemplo 1

```python
>>> x = 1    # int
>>> y = 2.8  # float
>>> z = 1j   # complex
```

### Tipos de sequência

Os tipos de sequência em Python são `list`, `tuple`, `range` e `str`.

#### Exemplo 1

```python   
>>> x = ["apple", "banana", "cherry"] # list
>>> y = ("apple", "banana", "cherry") # tuple
>>> z = range(6)                     # range
>>> w = "banana"                     # str
```

### Tipos de mapeamento

O tipo de mapeamento em Python é `dict`.

#### Exemplo 1

```python
>>> x = {"name" : "John", "age" : 36} # dict
```

### Tipos de conjunto

Os tipos de conjunto em Python são `set` e `frozenset`.

#### Exemplo 1

```python
>>> x = {"apple", "banana", "cherry"} # set
>>> y = frozenset({"apple", "banana", "cherry"}) # frozenset
```

### Tipos booleanos

O tipo booleano em Python é `bool`.

#### Exemplo 1

```python
>>> x = True
>>> y = False
```

### Tipos binários

O tipo binário em Python é `bytes`.

#### Exemplo 1

```python
>>> x = b"Hello"
```

### Tipos byte

O tipo byte em Python é `bytearray`.

#### Exemplo 1

```python
>>> x = bytearray(5)
```

### Tipos de memória

Os tipos de memória em Python são `memoryview` e `buffer`.

#### Exemplo 1

```python
>>> x = memoryview(bytes(5))
```

### Tipos de dados definidos pelo usuário

Os tipos de dados definidos pelo usuário em Python são `class` e `module`.

#### Exemplo 1

```python
>>> class MyClass:
...     x = 5
...
>>> p1 = MyClass()
>>> print(p1.x)
5
```

## Variáveis globais

Variáveis globais são variáveis que podem ser usadas por qualquer parte do código.

### Exemplo 1

```python
>>> x = "awesome"

>>> def myfunc():
...   print("Python is " + x)

>>> myfunc()
Python is awesome
```
