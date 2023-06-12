# Módulos em Python 

Módulos são arquivos Python que podem ser importados em outros arquivos Python.

## Criando um módulo

Para criar um módulo, criamos um arquivo com a extensão .py e escrever o código desejado. Além disso, é necessário criar um arquivo chamado __init__.py para que o Python reconheça o diretório como um módulo. 

Exemplo de um módulo:

```python
# modulos\meu_modulo.py

def soma(a, b):
    return a + b
```

```python
# modulos\__init__.py

# arquivo vazio
```

## Importando um módulo

Para importar um módulo, utilizamos a palavra reservada import seguida do nome do módulo.

```python
# importando o módulo criado anteriormente
import meu_modulo

# chamando a função soma do módulo
resultado = meu_modulo.soma(1, 2)
print(resultado)
```



