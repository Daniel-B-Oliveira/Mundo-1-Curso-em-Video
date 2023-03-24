# 017 - Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente
#       de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.
cat1 = float(input('Valor da hipotenusa de um triângulo retângulo'
                   '\nValor do \033[31mprimeiro\033[m cateto (\033[31mAB\033[m): '))
cat2 = float(input('Valor do \033[32msegundo\033[m cateto (\033[32mBC\033[m): '))
print(f'\nO valor da \033[33mhipotenusa\033[m do triangulo de segmentos: \033[31m{cat1}\033[m '
      f'; \033[32m{cat2}\033[m ; \033[33mAC\033[m = \033[33m{float((cat1**2+cat2**2)**(1/2)):.3f}\033[33m')
