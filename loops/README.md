# Laços de repetição em Python 

Os laços de repetição são estruturas de controle que permitem executar um bloco de código várias vezes.

## Laço for

O laço for é usado para iterar sobre uma sequência (lista, tupla, dicionário, conjunto ou string).

### Exemplo 1

```python
>>> for i in range(5):
...     print(i)

saída:
...
0
1
2
3
4
```

### Exemplo 2

```python
>>> for i in range(5, 10):
...     print(i)

saída:
...
5
6
7
8
9
```

### Exemplo 3

```python

>>> for i in range(0, 10, 3):
...     print(i)

saída:
...
0
3
6
9
```

### Exemplo 4

```python
>>> for i in range(-10, -100, -30):
...     print(i)

saída:
...
-10
-40
-70
```

## Laço while

O laço while é usado para executar um bloco de código enquanto uma condição for verdadeira.

### Exemplo 1

```python
>>> i = 1
>>> while i < 6:
...     print(i)
...     i += 1

saída:
...
1
2
3
4
5
```

