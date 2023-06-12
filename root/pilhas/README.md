# Estrutura de dados: Pilha 

## Pilha

Uma pilha é uma estrutura de dados que segue o princípio LIFO (Last In, First Out), ou seja, o último elemento a entrar é o primeiro a sair. Podemos fazer analogia com uma pilha de pratos, onde o último prato a ser colocado na pilha é o primeiro a ser retirado. 

Imagine você em um restaurante com self-service, você vai até a pilha de pratos e o prato que você vai pegar é o que está no topo da pilha. 

Para implementar uma pilha, podemos utilizar uma lista, uma vez que a lista já possui os métodos necessários para a manipulação de uma pilha.

Vamos criar uma classe Pilha que herda de list, e que implementa os métodos push e pop.

### Classe Pilha

```python
class Pilha(list):
    def push(self, item):
        self.append(item)

    def pop(self):
        return super().pop()
```

No exemplo a seguir, vamos criar uma pilha e inserir alguns elementos nela. Em seguida, vamos retirar os elementos da pilha, e veremos que o último elemento a entrar é o primeiro a sair.

### Exemplo

```python
from pilhas import Pilha

pilha = Pilha()

pilha.push(1)
pilha.push(2)
pilha.push(3)

print(pilha.pop()) # 3
print(pilha.pop()) # 2
print(pilha.pop()) # 1
```

## Métodos

### push

O método push insere um elemento no topo da pilha.

### pop

O método pop remove o elemento do topo da pilha e o retorna.


# Exercícios


Crie uma classe Pilha que implemente os métodos push e pop, utilizando uma lista como atributo. A classe Pilha deve ter um atributo que indique o tamanho máximo da pilha. A classe Pilha deve ter um atributo que indique o tamanho atual da pilha.


