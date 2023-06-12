# Condicionais em Python 

## IF

O if é uma estrutura de decisão que permite executar um bloco de código caso uma condição seja verdadeira. 

```python
if condicao:
    # bloco de código
```

## ELSE

O else é uma estrutura de decisão que permite executar um bloco de código caso uma condição seja falsa. 

```python
if condicao:
    # bloco de código
else:
    # bloco de código
```

## ELIF

O elif é uma estrutura de decisão que permite executar um bloco de código caso uma condição seja verdadeira. 

```python

if condicao:
    # bloco de código
elif condicao:
    # bloco de código
else:
    # bloco de código
```

## Operadores de comparação

| Operador | Descrição |
|:--------:|:---------:|
| == | Igual |
| != | Diferente |
| > | Maior que |
| < | Menor que |
|<= | Menor ou igual a |
|>= | Maior ou igual a |


## Operadores lógicos

| Operador | Descrição |
|:--------:|:---------:|
| and | E |
| or | Ou |
| not | Negação |

## Operadores de identidade

| Operador | Descrição |
|:--------:|:---------:|
| is | É |
| is not | Não é |

## Operadores de associação

| Operador | Descrição |
|:--------:|:---------:|
| in | Está contido |
| not in | Não está contido |

## Exemplos

### IF

```python
if 1 == 1:
    print("1 é igual a 1")
```

### ELSE

```python
if 1 == 2:
    print("1 é igual a 2")
else:
    print("1 é diferente de 2")
```

### ELIF

```python

if 1 == 2:
    print("1 é igual a 2")
elif 1 == 1:
    print("1 é igual a 1")
else:
    print("1 é diferente de 2")
```

### Operadores de comparação

```python
if 1 == 1:
    print("1 é igual a 1")

if 1 != 2:
    print("1 é diferente de 2")

if 1 > 2:
    print("1 é maior que 2")

if 1 < 2:
    print("1 é menor que 2")

if 1 <= 2:
    print("1 é menor ou igual a 2")

if 1 >= 2:
    print("1 é maior ou igual a 2")
```

### Operadores lógicos

```python
if 1 == 1 and 2 == 2:
    print("1 é igual a 1 e 2 é igual a 2")

if 1 == 1 or 2 == 2:
    print("1 é igual a 1 ou 2 é igual a 2")

if not 1 == 2:
    print("1 é diferente de 2")
```

### Operadores de identidade

```python
if 1 is 1:
    print("1 é igual a 1")

if 1 is not 2:
    print("1 é diferente de 2")
```

### Operadores de associação

```python
lista = [1, 2, 3, 4, 5]

if 1 in lista:
    print("1 está contido na lista")

if 6 not in lista:
    print("6 não está contido na lista")
```

## Exercícios

1. Crie um programa que receba um número e verifique se ele é par ou ímpar.

2. Crie um programa que receba um número e verifique se ele é positivo ou negativo.

3. Crie um programa que receba um número e verifique se ele é maior que 10.

4. Crie um programa que receba um número e verifique se ele é maior que 10 e menor que 20.

5. Crie um programa que receba um número e verifique se ele é maior que 10 e menor que 20 ou se ele é igual a 30.

6. Crie um programa que receba um número e verifique se ele é maior que 10 e menor que 20 ou se ele é igual a 30 ou se ele é maior que 40.


