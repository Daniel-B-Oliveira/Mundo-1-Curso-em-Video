# 032 - Faça um programa que leia um ano qualquer e mostre se ele é bissexto.

from datetime import date

ano = int(input('Digite um ano (Digite 0 para analisar o ano atual): '))
if ano == 0:
    ano = date.today().year

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'\n\033[32m{ano} é bissexto\033[m')
else:
    print(f'\n\033[31m{ano} não é bissexto\033[m')
