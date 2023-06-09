# Manipulando arquivos na linguagem Python 

## O que é um arquivo?

Um arquivo é um conjunto de dados gravados em um dispositivo de armazenamento permanente. Um arquivo pode ser qualquer tipo de dado, como um documento, uma imagem, um vídeo, um programa, etc.

## Como abrir um arquivo?

Para abrir um arquivo, utilizamos a função `open()`. Essa função recebe dois parâmetros: o nome do arquivo e o modo de abertura do arquivo.

```python
    arquivo = open('arquivo.txt', 'r')
```

O primeiro parâmetro é o nome do arquivo que queremos abrir. O segundo parâmetro é o modo de abertura do arquivo. O modo de abertura do arquivo é uma string que pode ser:

- `'r'`: abre o arquivo para leitura (padrão);
- `'w'`: abre o arquivo para escrita. Se o arquivo não existir, cria um novo arquivo. Se o arquivo existir, apaga o conteúdo do arquivo;
- `'a'`: abre o arquivo para escrita. Se o arquivo não existir, cria um novo arquivo. Se o arquivo existir, escreve o conteúdo no final do arquivo;
- `'x'`: abre o arquivo para escrita. Se o arquivo não existir, cria um novo arquivo. Se o arquivo existir, retorna um erro;
- `'t'`: abre o arquivo em modo texto (padrão);
- `'b'`: abre o arquivo em modo binário.

## Como ler um arquivo?

Para ler um arquivo, utilizamos a função `read()`. Essa função não recebe parâmetros.

```python
    arquivo = open('arquivo.txt', 'r')
    conteudo = arquivo.read()
```

## Como escrever em um arquivo?

Para escrever em um arquivo, utilizamos a função `write()`. Essa função recebe um parâmetro: o conteúdo que queremos escrever no arquivo.

```python
    arquivo = open('arquivo.txt', 'w')
    arquivo.write('Olá, mundo!')
```

## Como fechar um arquivo?

Para fechar um arquivo, utilizamos a função `close()`. Essa função não recebe parâmetros.

```python
    arquivo = open('arquivo.txt', 'r')
    conteudo = arquivo.read()
    arquivo.close()
```

## Como ler uma linha de um arquivo?

Para ler uma linha de um arquivo, utilizamos a função `readline()`. Essa função não recebe parâmetros.

```python
    arquivo = open('arquivo.txt', 'r')
    linha = arquivo.readline()
```

## Como ler todas as linhas de um arquivo?

Para ler todas as linhas de um arquivo, utilizamos a função `readlines()`. Essa função não recebe parâmetros.

```python
    arquivo = open('arquivo.txt', 'r')
    linhas = arquivo.readlines()
```

A função `readlines()` retorna uma lista com todas as linhas do arquivo. Dessa forma, podemos percorrer a lista com um laço de repetição `for`.

```python
    arquivo = open('arquivo.txt', 'r')
    linhas = arquivo.readlines()
    for linha in linhas:
        print(linha)
```

Ou ainda podemos ler as linhas do arquivo diretamente com um laço de repetição `for`. 
Para ler um arquivo linha a linha utilizamos o laço de repetição `for`. O laço de repetição `for` percorre cada linha do arquivo.

```python
    arquivo = open('arquivo.txt', 'r')
    for linha in arquivo:
        print(linha)
```

## Escrevendo em um arquivo

Para escrever em um arquivo, utilizamos a função `write()`. Essa função recebe um parâmetro: o conteúdo que queremos escrever no arquivo.

```python
    arquivo = open('arquivo.txt', 'w')
    arquivo.write('Olá, mundo!')
```

## Exemplo

### Exemplo 1

Escreva um programa que leia um arquivo texto e imprima o conteúdo do arquivo na tela.

#### Arquivo texto

```python
    arquivo = open('arquivo.txt', 'r')
    conteudo = arquivo.read()
    print(conteudo)
```

#### Resultado

```python
    Olá, mundo!
```

### Exemplo 2

Escreva um programa que leia um arquivo texto e imprima o conteúdo do arquivo na tela linha a linha.

#### Arquivo texto

```python
    arquivo = open('arquivo.txt', 'r')
    for linha in arquivo:
        print(linha)
```

### Exemplo 3 

Escreva um programa que escreva o conteúdo de uma lista em um arquivo texto.

#### Arquivo texto

```python
    lista = ['Olá', 'mundo', '!']
    arquivo = open('arquivo.txt', 'w')
    for item in lista:
        arquivo.write(item + '\n')
```



1. Prática 01 ✅[(clique aqui para ver as questões)](https://github.com/roscibely/algorithms-and-data-structure/blob/develop/arquivos/quest%C3%B5es-pr%C3%A1tica-01-arquivos.pdf):  
  
   1️⃣ [Acesse a resposta em Python da questão 1](https://github.com/roscibely/data-structure-with-python/blob/main/arquivos/pratica_q1.py) 
    
 
   2️⃣ [Acesse a resposta em Python da questão 2](https://github.com/roscibely/data-structure-with-python/blob/main/arquivos/pratica-q2.py) 

## [Veja mais exemplos](https://github.com/roscibely/data-structure-with-python/blob/main/arquivos/intro_arquivos.ipynb)

Veja um exemplo [aqui](https://github.com/roscibely/data-structure-with-python/blob/develop/arquivos/exemplo_1.py)
