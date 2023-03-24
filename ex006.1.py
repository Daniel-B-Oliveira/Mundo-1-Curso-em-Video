# 028 - Escreva um programa que faça o computador "pensar" em um número
#       inteiro entre 0 e 5 e peça para o usuário tentar descobrir
#       qual foi o número escolhido pelo computador.
#       O programa deverá escrever na tela se o usuário venceu ou perdeu.
from random import randint

num0 = randint(0, 5)
num1 = int(input('Tente adivinhar o número sorteado\nDigite um número de 0 a 5: '))
if num0 == num1:
    print(f'\nVocê \033[32macertou\033[m, o número escolhido era \033[32m{num0}\033[m\n'
          f'Fim de Jogo, você \033[32mvenceu\033[m.')
else:
    if num1 > 5:
        print(f'\n\033[31m{num1}\033[m está entre \033[33m0\033[m e \033[33m5\033[m?'
              f'\nO número escolhido era \033[32m{num0}\033[m\n'
              f'Fim de Jogo, você \033[31mperdeu\033[m.')
    else:
        print(f'\nQue pena, o número  era \033[32m{num0}\033[m, você escolheu \033[31m{num1}\033[m'
              f'\nFim de Jogo, você \033[31mperdeu\033[m.')
