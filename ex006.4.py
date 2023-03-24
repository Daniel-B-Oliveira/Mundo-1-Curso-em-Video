#  031: Desenvolva um programa que pergunte a distância de uma viagem em Km.
#       Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km
#       e R$0,45 parta viagens mais longas.

d1 = float(input('Qual a distância da sua viagem desejada? '))
if d1 > 200:
    print(f'O valor da pasagem será de \033[32mR${float(d1 * 0.45):.2f}\033[m')
else:
    print(f'O valor da pasagem será de \033[33mR${float(d1 * 0.5):.2f}\033[m')
