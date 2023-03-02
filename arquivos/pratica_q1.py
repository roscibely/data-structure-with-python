"""
  Questão 1:

Escreva um programa que leia do arquivo entrada_q3.txt
as notas dos alunos de uma turma e calcule a média de cada
aluno. O programa deve escrever o nome do aluno e sua média
em um arquivo de saída chamado saida_q3.txt, bem como
a situação do aluno (aprovado ou reprovado). A média para
aprovação é 7.0. O arquivo de entrada possui o seguinte
formato:

    João da Silva 8.0 7.0 6.0
    Maria da Silva 9.0 8.0 7.0
    José da Silva 6.0 5.0 4.0

    O arquivo de saída deve ter o seguinte formato:

    João da Silva 7.0 Aprovado
    Maria da Silva 8.0 Aprovado
    José da Silva 5.0 Reprovado

"""

# Abrindo o arquivo de entrada
arquivo_entrada = open('arquivos/entrada_q3.txt', 'r')

# Abrindo/Criando o arquivo de saída
arquivo_saida = open('arquivos/saida_q3.txt', 'w')

# Lendo o arquivo de entrada
linhas = arquivo_entrada.readlines()

# Percorrendo as linhas do arquivo de entrada
for linha in linhas:
    # Separando o nome do aluno das notas os dados da linha estão separados por \t
    nome, nota1, nota2, nota3 = linha.split('\t')
    # Calculando a média
    media = (float(nota1) +float(nota2)+float(nota3)) / 3
    # Escrevendo no arquivo de saída
    arquivo_saida.write(f'{nome} {media} {"Aprovado" if media >= 7 else "Reprovado"}\r ' )

# Fechando os arquivos
arquivo_entrada.close()
arquivo_saida.close()

