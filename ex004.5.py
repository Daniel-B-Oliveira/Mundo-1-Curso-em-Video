# 020 - O mesmo professor do desafio 019 quer sortear a ordem de apresentação
#       de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos
#       e mostre a ordem sorteada.
# OBS: Não sei como mudar as cores

from random import shuffle

aln0 = str(input('Coloque o nome do primeiro aluno(a)'))
aln1 = str(input('Coloque o nome do segundo aluno(a)'))
aln2 = str(input('Coloque o nome do terceiro aluno(a)'))
aln3 = str(input('Coloque o nome do quarto aluno(a)'))

ch = [aln0, aln1, aln2, aln3]
shuffle(ch)

print(f'\nSequência:\n{ch}')
