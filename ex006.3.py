#  030 - Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.

num0 = int(input('Digite um número para saber se ele é par ou ímpar'))
if num0 % 2 == 0:
    print(f'\n\033[32mSim\033[m, \033[36m{num0}\033[m é par')
else:
    print(f'\n\033[31mNão\033[m, \033[36m{num0}\033[m é impar')
