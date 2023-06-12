# Ponteiros em Python 

Um ponteiro é uma variável que armazena o endereço de memória de outra variável. Em Python, não há ponteiros, mas podemos simular o comportamento de ponteiros usando o módulo `ctypes`. 

## O módulo `ctypes`

O módulo `ctypes` é um módulo Python que fornece uma maneira de usar tipos de dados C em Python. Ele fornece uma maneira de carregar bibliotecas dinâmicas e acessar seus recursos. Ele pode ser usado para criar arrays de dados e manipular strings.

## Criando um ponteiro

Para criar um ponteiro, usamos a função `pointer()` do módulo `ctypes`. Essa função recebe como parâmetro o tipo de dado que o ponteiro irá apontar. 

```python
from ctypes import pointer, c_int

ponteiro = pointer(c_int(10)) # ponteiro apontando para um inteiro

```

## Acessando o valor apontado

Para acessar o valor apontado, usamos a função `contents` do módulo `ctypes`. 

```python
from ctypes import pointer, c_int

ponteiro = pointer(c_int(10))

print(ponteiro.contents)
```

## Alterando o valor apontado

Para alterar o valor apontado, usamos a função `contents` do módulo `ctypes`. 

```python
from ctypes import pointer, c_int

ponteiro = pointer(c_int(10))

ponteiro.contents = 20 # alterando o valor apontado

print(ponteiro.contents)
```

## Acessando o endereço de memória

Para acessar o endereço de memória, usamos a função `addressof` do módulo `ctypes`. 

```python
from ctypes import pointer, c_int, addressof

ponteiro = pointer(c_int(10))

print(addressof(ponteiro.contents))
```

## Acessando o tipo de dado apontado

Para acessar o tipo de dado apontado, usamos a função `type` do módulo `ctypes`. 

```python
from ctypes import pointer, c_int, addressof

ponteiro = pointer(c_int(10))

print(type(ponteiro.contents))
```

## Acessando o tamanho do tipo de dado apontado

Para acessar o tamanho do tipo de dado apontado, usamos a função `sizeof` do módulo `ctypes`. 

```python
from ctypes import pointer, c_int, addressof, sizeof

ponteiro = pointer(c_int(10))

print(sizeof(ponteiro.contents))
```

## Acessando o valor apontado por um ponteiro

Para acessar o valor apontado por um ponteiro, usamos a função `value` do módulo `ctypes`. 

```python
from ctypes import pointer, c_int, addressof, sizeof, value

ponteiro = pointer(c_int(10))

print(value(ponteiro))
```

## Acessando o valor apontado por um ponteiro

Para acessar o valor apontado por um ponteiro, usamos a função `value` do módulo `ctypes`. 

```python
from ctypes import pointer, c_int, addressof, sizeof, value

ponteiro = pointer(c_int(10))

print(value(ponteiro))
```


Ponteiros em Python são implementados como referências. Referências são ponteiros que apontam para objetos. Ou seja, uma referência é um endereço de memória que armazena o endereço de um objeto.

## Exemplo 1

```python
>>> x = 5
>>> y = x
>>> x = 10
>>> print(y)
5
```

## Exemplo 2

```python
>>> x = ["apple", "banana"]
>>> y = x
>>> x[0] = "cherry"
>>> print(y)
['cherry', 'banana']
```

## Exemplo 3

```python
>>> x = ["apple", "banana"]
>>> y = x
>>> x = ["cherry", "orange"]
>>> print(y)
['apple', 'banana']
```

