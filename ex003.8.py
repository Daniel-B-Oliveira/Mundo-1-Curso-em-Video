# 012 - Faça um algortimo que leia o preço de um produto  e mostre seu novo preço ,
# com 5% de desonto

c = {'n': '\033[m',
     'w': '\033[30m',
     'r': '\033[31m',
     'g': '\033[32m',
     'y': '\033[33m',
     'b': '\033[34m',
     'p': '\033[35m',
     'c': '\033[36m',
     's': '\033[37m', }

v = float(input('Insira o valor de um  produto: '))
print('')  # O \n não tava funcionando =(
perg = str(input('Digiti {0}0{4} se deseja fazer um {1}desconto{5}; '
                 'digite {2}qualquer tecla{6} se deseja fazer um {3}acrescimo{7}'
                 .format(c['g'], c['g'], c['r'], c['r'], c['n'], c['n'], c['n'], c['n']).strip()))
if perg == '0':
    i = float(input('Qual será a porcentagem deste \033[32mdesconto\033[m? ')) / -100 + 1
    p = '\033[32mdesconto\033[m'
else:
    i = float(input('Qual será a porcentagem deste \033[31macrescimo\033[m? ')) / 100 + 1
    p = '\033[31macrescimo\033[m'

print(f'\nO valor do produto com {p} será de \033[36mR${i*v:.2f}\033[m')
