# 008 - escreva um programa que leia um valor em metros
#       e o exiba convertido em centimetros e milimetros
#       retomar exercicios aula 11 (10/03)
n = float(input('escreva um valor me metros'))

print('{}{}{} dm'.format('\033[32m', float(n*10**1), '\033[m'))
print('{}{}{} cm'.format('\033[33m', float(n*10**2), '\033[m'))
print('{}{}{} mm'.format('\033[31m', float(n*10**3), '\033[m'))
