# Definição de Funções com Python 3 

## Definição de Funções

Uma função é um bloco de código que executa uma tarefa específica. Uma função é definida usando a palavra-chave def. A sintaxe é a seguinte:

```python
def nome_da_funcao():
    # código da função
```

As funções são importantes para a reutilização de código. Por exemplo, se você precisar executar a mesma tarefa várias vezes, você pode definir uma função para executar essa tarefa e, em seguida, chamar a função sempre que você precisar executar a tarefa.

## Chamando uma Função

Para chamar uma função, digite o nome da função seguido de parênteses:

```python
nome_da_funcao()
```

## Argumentos

As funções podem receber argumentos. Os argumentos são especificados após o nome da função, dentro dos parênteses. Você pode adicionar quantos argumentos quiser, basta separá-los com uma vírgula.

Os argumentos são frequentemente abreviados como args.

O exemplo abaixo tem uma função com um argumento (fname). Quando a função é chamada, passamos um argumento, ou valor, que é usado dentro da função para imprimir o nome completo:

```python
def nome_completo(fname):
    print(fname + " Santos")

nome_completo("João")
nome_completo("Maria")
nome_completo("José")
```

## Número Arbitrário de Argumentos

Se você não souber quantos argumentos que serão passados para sua função, adicione um * antes do nome do parâmetro na definição da função.

Isso fará com que o parâmetro receba uma tupla de argumentos e você pode acessar os itens de acordo com a necessidade.

```python
def nome_completo(*nomes):
    print("O nome completo é: " + nomes[0] + " " + nomes[1])

nome_completo("João", "Santos")
nome_completo("Maria", "Santos")
nome_completo("José", "Santos")
```

## Parâmetros de Palavra-chave

Se você quiser que uma função receba um número fixo de argumentos, adicione dois pontos (:) após o parâmetro e, em seguida, defina os valores padrão para os parâmetros. Isso fará com que o parâmetro seja opcional.

```python
def nome_completo(nome, sobrenome = "Santos"):
    print(nome + " " + sobrenome)

nome_completo("João")
nome_completo("Maria")
nome_completo("José")
```

## Retornando Valores

Para deixar uma função retornar um valor, use a instrução return:

```python
def soma(x, y):
    return x + y

print(soma(5, 3))
```

## Recursão

Uma função pode chamar a si mesma. Isso é chamado de recursão.

A função abaixo imprime uma sequência de números, começando em 0, e terminando em 10:

```python
def recursao(i):
    if (i < 10):
        print(i)
        recursao(i + 1)

recursao(0)
```

## Exemplo:Resolvendo o Fatorial com recursão

O fatorial de um número é o produto de todos os inteiros inferiores a e incluindo ele mesmo. O fatorial de 5 é escrito como 5! e é igual a 1 * 2 * 3 * 4 * 5 = 120. Escreva uma função que calcule o fatorial de um número.

```python
def fatorial(n):
    if n == 1:
        return 1
    else:
        return n * fatorial(n - 1)

print(fatorial(5))
```

## Exemplo: Resolvendo o Fibonacci com recursão

O número de Fibonacci é uma sequência de números inteiros, começando normalmente por 0 e 1, na qual, cada termo subsequente corresponde à soma dos dois anteriores. Escreva uma função que calcule o n-ésimo número de Fibonacci.

```python

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return(fibonacci(n-1) + fibonacci(n-2))

print(fibonacci(9))

```

## Função Lambda

Uma função lambda é uma pequena função anônima.

Uma função lambda pode receber qualquer número de argumentos, mas pode ter apenas uma expressão.

```python

x = lambda a : a + 10
print(x(5))

```

## Função Map

A função map() aplica uma função a todos os itens de um iterável.

```python

def dobro(x):
    return x * 2

valores = [1, 2, 3, 4, 5]

valores_dobrados = map(dobro, valores)

print(list(valores_dobrados))

```

## Função Filter

A função filter() cria uma lista de elementos para os quais uma função retorna True.

```python

def maior_que_5(x):
    if x > 5:
        return True
    else:
        return False

valores = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

valores_maiores_que_5 = filter(maior_que_5, valores)

print(list(valores_maiores_que_5))

```



