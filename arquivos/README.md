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

## Como ler um arquivo linha a linha?

Para ler um arquivo linha a linha, utilizamos a função `readline()`. Essa função não recebe parâmetros.

```python
    arquivo = open('arquivo.txt', 'r')
    for linha in arquivo:
        print(linha)
```

Veja um exemplo [aqui](https://github.com/roscibely/data-structure-with-python/blob/develop/arquivos/exemplo_1.py)
