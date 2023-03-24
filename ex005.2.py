# 023 - Faça um programa que leia um número de 0 a 9999
#       e mostre na tela cada um dos dígitos separados.

b0 = str(float(int(input('Digite um número qualquer, entre 0 e 9999: '))/10000))[2:]
print(f'   m: \033[31m{b0[0]}000\033[m\n   c: \033[32m0{b0[1]}00\033[m\n'
      f'   d: \033[33m00{b0[2]}0\033[m\n + u: \033[34m000{b0[3]}\033[m\n' + '-'*11 + f'\n      \033[35m{b0}\033[m')
