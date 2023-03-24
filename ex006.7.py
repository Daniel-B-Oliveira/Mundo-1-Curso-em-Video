#  034 - Escreva um programa que pergunte o salário de um funcionário e calcule o valor
#       do seu aumento. Para salários superiores a R$1250,00, calcule um aumento de 10%.
#       Para os inferiores ou iguais, o aumento é de 15%.

sal0 = float((input('Qual o valor do seu salário')))
if sal0 > 1250:
    print(f'Seu salário passou por um \033[32mreajuste\033[m e será de: \033[36mR${sal0 * 1.1:.2f}\033[m')
else:
    print(f'Seu salário passou por um \033[32mreajuste\033[m e será de: \033[36mR${sal0 * 1.15:.2f}\033[m')
