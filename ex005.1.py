# 022 - Crie um programa que leia o nome completo de uma pessoa e mostre:
# - O nome com todas as letras maiúsculas e minúsculas.
# - Quantas letras ao todoo (sem considerar espaços).
# - Quantas letras tem o primeiro nome.

name0 = str(input('Digite seu nome completo: '))
print(f'\n{name0.upper()}\n{name0.lower()}\nnúmero de letras: {len(name0.replace(" ", "").strip())}'
      f'\nnúmero de letras do primeiro nome: {len((name0.split()[0]))}')
