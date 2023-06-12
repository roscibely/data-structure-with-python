# Class na Liguagem Python 

## O que é uma classe?

Na programação orientada a objetos, uma classe é um modelo que define os atributos e métodos comuns a todos os objetos de um determinado tipo. Uma classe é uma estrutura que contém dados e métodos que podem ser utilizados por todos os objetos criados a partir dela. 

Se fizermos analogia com uma linguagem estruturada como a linguagem C, podemos dizer que uma classe é uma estrutura que contém dados e métodos que podem ser utilizados por todos os objetos criados a partir dela.

## O que é um objeto?

Um objeto pode ser definido como uma instância de uma classe. Um objeto é uma entidade que possui estado e comportamento. O estado de um objeto é armazenado em campos (variáveis) de dados e o comportamento é definido por métodos. 

## O que é um método?

Um método pode ser definido como um bloco de código que é executado quando é chamado. Um método é basicamente um procedimento associado a um objeto. Um método é semelhante a uma função, com a diferença de que um método está associado a um objeto e é executado quando é chamado por um objeto.

Exemplo:

```python
    class Pessoa:
        def __init__(self, nome, idade):
            """
            Construtor da classe Pessoa
            """
            self.nome = nome
            self.idade = idade
    
        def falar(self):
            """ Método que imprime o nome e a idade da pessoa """

            print(f'Olá, meu nome é {self.nome} e tenho {self.idade} anos.')
```
Declaração de uma classe chamada Pessoa. A classe possui dois atributos: nome e idade. A classe também possui um método chamado falar.

A seguir, criamos um objeto da classe Pessoa e chamamos o método falar.

```python
    p1 = Pessoa('João', 32)
    p1.falar()
```

Se fizermos analogia com a linguagem C, podemos dizer que um método é uma função que está associada a uma estrutura. E que o construtor é como a estrutura em si, onde fazemos a declaração dos campos (variáveis) de dados.


Exemplo em C:

```c
    struct Pessoa {
        char nome[50];
        int idade;
    };
    
    void falar(struct Pessoa p) {
        printf("Olá, meu nome é %s e tenho %d anos.", p.nome, p.idade);
    }
```

A seguir, criamos um objeto da estrutura Pessoa e chamamos a função falar.

```c
    struct Pessoa p1 = {"João", 32};
    falar(p1);
```

