# 033 - Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

a = int(input('Insira o primeiro número'))
b = int(input('Insirua o segundo número'))
c = int(input('Insira o terceiro número'))

menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c

maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c

print(f'\nO \033[32mmaior\033[m valor é: \033[32m{maior}\033[m')
print(f'\nO \033[31mmenor\033[m valor é: \033[31m{menor}\033[m')
