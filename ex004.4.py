# 019 - Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
#       Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.
from random import choice

aln0 = str(input('Coloque o nome do primeiro aluno(a)'))
aln1 = str(input('Coloque o nome do segundo aluno(a)'))
aln2 = str(input('Coloque o nome do terceiro aluno(a)'))
aln3 = str(input('Coloque o nome do quarto aluno(a)'))

chs = (aln0, aln1, aln2, aln3)
print(f'\nO aluno(a) escolhido foi: \033[31m{choice(chs)}\033[m')
