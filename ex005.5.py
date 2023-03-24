# 026 - Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece
#       a letra "A", em que posição ela aparece a primeira vez e
#       em que posição ela aparece a última vez

prg0 = str("A")    # Caracter(es) pesquisado

frs0 = str(input('Escreva um frase: ')).strip()

print(f'\nFrase: "\033[36m{frs0}\033[m"'
      f'\nOcorrêcia(s) de "\033[31m{prg0}\033[m": {(frs0.count(prg0, 0))}'
      f'\nPrimeira Ocorrência de "\033[31m{prg0}\033[m": 'f'{(frs0.find(prg0))}'
      f'\nÚltima Ocorrência de "\033[31m{prg0}\033[m": {(frs0.rfind(prg0))}')

print(f'\nSem considera maiúscula e minúscula: \n'
      f'\nFrase: "\033[36m{frs0.lower()}\033[m"'
      f'\nOcorrêcia(s) de "\033[31m{prg0.lower()}\033[m": {(frs0.lower().count(str(prg0.lower()), 0)) }'
      f'\nPrimeira Ocorrência de "\033[31m{prg0.lower()}\033[m": {(frs0.lower().find(prg0.lower()))}'
      f'\nÚltima Ocorrência de "\033[31m{prg0.lower()}\033[m": {(frs0.lower().rfind(prg0.lower()))}')
