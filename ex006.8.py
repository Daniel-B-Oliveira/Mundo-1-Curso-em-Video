# 035 - Desenvolva um programa que leia o comprimento de três retas e diga ao usuário
#       se elas podem ou não formar um triângulo

a = float(input('Insira o comprimento do primero lado do triângulo'))
b = float(input('Insira o comprimento do segundo lado do triângulo'))
c = float(input('Insira o comprimento do teceiro lado do triângulo'))

if a + b > c and a + c > b and b + c > a:
    print('\n\033[32mAs retas podem formar um triângulo\033[m')
else:
    print('\n\033[31mAs não retas podem formar um triângulo\033[m')
