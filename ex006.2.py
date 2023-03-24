# 029 - Escreva um programa que leia a velocidade de um carro.
#       Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
#       A multa vai custar R$7,00 por cada Km acima do limite.

from random import randint

vmax = int(80)
val0 = float(7)

v = int(input('A qual velocidade o carro do individuo estava(Km/h)? '))

if v <= vmax:
    if v < vmax * 0.5:
        n = randint(0, 4)
        if n == 0:
            print(f'\nSua Velocidade foi de \033[33m{v}Km/h\033[m, {int(vmax - v)}Km/h abaixo do permitido.'
                  f'\nNesse caso, não houve interferência na circulação da via. '
                  f'\nOBS: \033[32mIndivio deve ser liberado\033[32m')
        else:
            if v == 1:  # V precisa ser diferente de 1 para que não ocorra uma divisão por 0
                print(f'\nSua Velocidade foi de \033[33m{v}Km/h\033[m, {int(vmax - v)}Km/h abaixo do permitido.'
                      f'\nNesse caso, houve interferência na circulação da via.'
                      f'\nO valor da multa será de '
                      f'\033[33mR${(float(203.9286668447769)):.2f}'
                      f'\033[m'
                      f'\nOBS: \033[31mAcompanhamento na delegacia não obrigatório\033[m')
            else:
                print(f'\nSua Velocidade foi de \033[33m{v}Km/h\033[m, {int(vmax - v)}Km/h abaixo do permitido.'
                      f'\nNesse caso, houve interferência na circulação da via.'
                      f'\nO valor da multa será de '
                      f'\033[33mR${(float((vmax-v)*val0/(1-(1/v)))/7.2):.2f}'
                      f'\033[m'
                      f'\nOBS: \033[31mAcompanhamento na delegacia não obrigatório\033[m')

    else:
        print('\nSua velocidade estava entre a miníma e a máxima\n'
              'OBS: \033[32mIndivio deve ser liberado\033[m')
else:
    if v > (vmax * 1.9):
        print(f'\nSua velocidade foi de \033[31m{v}Km/h\033[m, {(v - vmax)}Km/h ácima do permitido.'
              f'\nO valor da multa será de '
              f'\033[31mR${(float((v-vmax)*(val0/100)*v)):.2f}\033[m'
              f'\nOBS: \033[7;31mIndivio deve ser preso\033[m')
    else:
        print(f'\nSual velocidade foi de \033[33m{v}Km/h\033[m, {(v - vmax)}Km/h ácima do permitido.'
              f'\nO valor da multa será de \033[33mR${float((v - vmax) * val0)}\033[m'
              f'\nOBS: \033[31mAcompanhamento na delegacia não obrigatório\033[m')
