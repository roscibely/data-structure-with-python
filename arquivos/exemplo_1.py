#Exercício: Crie um arquivo e escreva nele os dados informados pelo o usuario: nome e telefone

# Importando o modulo os
import os

# Criando uma variavel para armazenar o nome do arquivo
arquivo = input('Digite o nome do arquivo: ')

# abrindo o arquivo para escrita
arquivo = open(arquivo, 'w')

# Criando uma variavel para armazenar o nome do usuario
nome = input('Digite o nome do usuario: ')

# Criando uma variavel para armazenar o telefone do usuario
telefone = input('Digite o telefone do usuario: ')

# Escrevendo os dados no arquivo
arquivo.write(nome + ' ' + telefone)

# Fechando o arquivo
arquivo.close()





