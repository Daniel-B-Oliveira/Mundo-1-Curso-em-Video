#  016 - Crie um programa que leia um número Real qualquer pelo teclado
#        e mostre na tela a sua porção Inteira.
from math import trunc

num = float(input('Coloque um número pertencente ao conjunto dos reais: '))

print(f'\nA parte inteira desse numero é: \033[31m{trunc(num)}\033[m'
      f'\n\033[31m{trunc(num)}\033[m + \033[32m{num-trunc(num):.3f}\033[m = {num:.3f}')
