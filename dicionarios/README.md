# Dicionários em Python 

Os dicionários são uma estrutura de dados que permite armazenar uma coleção de itens não ordenados. Cada item é composto por uma chave e um valor. Os itens podem ser de qualquer tipo, como números, strings, objetos, outras listas, etc.

Dicionários são estruturas de dados que podem armazenar vários valores. São mutáveis, ou seja, podemos alterar seus valores.

Em Python, os dicionários podem ser declarados da seguinte forma: 

```python

dicionario = {"chave1": "valor1", "chave2": "valor2"}

```

ou ainda 

```python

dicionario = dict()

```

Os dicionários são comumente utilizados em diversas aplicações no mundo real. Por exemplo, podemos armazenar os nomes e idades de todos os alunos de uma turma em um dicionário. 

```python

alunos = {"João": 20, "Maria": 19, "José": 21, "Ana": 18, "Pedro": 20}

```

Para acessar um valor de um dicionário, basta informar a chave correspondente. 

```python

alunos["João"] # 20

```

Os dicionários são mutáveis, o que significa que você pode adicionar, remover e alterar itens depois de criá-los. Exemplos:

```python

frutas = {"maçã": 2, "banana": 3, "laranja": 4}

# adicionar um item
frutas["manga"] = 5

# remover um item
del frutas["laranja"]

```





