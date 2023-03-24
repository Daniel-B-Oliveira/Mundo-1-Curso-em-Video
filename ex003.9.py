# 013 - Faça um algoritimo que leia o salário de um funcionário e mostre seu novo salário,
# com 15% de aumento
s = float(input('Qual o salário do funcionário? '))
i = float(input('\nQual a porcentagem de aumento desejada? '))
print(str(f'\nNovo salário: \033[36mR${s*(1+(i/100))}\033[m.'))
