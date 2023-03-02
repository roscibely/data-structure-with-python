"""
Questão 02 : 
Escreva um programa em python que preencha
um vetor de 10 inteiros com informações vindas de um arquivo
e escreva em outro arquivo o menor elemento, o maior elemento,
bem como a média dos elementos do vetor
"""

# Importando biblioteca
import numpy as np

# Abrindo arquivo
arquivo = open('arquivos\entrada_lista1_ex2.txt', 'r')

# Lendo arquivo
conteudo = arquivo.read()

# Fechando arquivo
arquivo.close() 

# Separando conteudo 
conteudo = conteudo.split() # o conteudo será um vetor de caracteres

# Convertendo conteudo para int
conteudo = [int(i) for i in conteudo]

# Calculando menor elemento com a função min()
menor = min(conteudo)

"""
Outra forma de calcular o menor elemento sem usar min()

menor = conteudo[0]
for i in conteudo:
    if i < menor:
        menor = i
    else:
        pass
"""

# Calculando maior elemento com a função max()
maior = max(conteudo)

"""
Outra forma de calcular o maior elemento sem usar max()

maior = conteudo[0]
for i in conteudo:
    if i > maior:
        maior = i
    else:
        pass
"""

# Calculando media com a função mean() da biblioteca numpy
media = np.mean(conteudo)
"""
Outra forma de calcular a media sem usar a função mean()

media = sum(conteudo) / len(conteudo)

len(conteudo) é tamanho do vetor
"""


# Escrevendo arquivo
arquivo = open('arquivos\saida_lista1_ex2.txt', 'w')

# Escrevendo conteudo

arquivo.write('Menor elemento: ' + str(menor) + ' ' + 'Maior elemento: ' + str(maior) + ' ' + 'Media: ' + str(media))

# Fechando arquivo
arquivo.close()


