# 006 - Crie um algoritimo que leia um número e mostre o seu dobro, triplo e raiz quadrada

c = {'n': '\033[m',
     'r': '\033[31m',
     'g': '\033[32m',
     'y': '\033[33m',
     'p': '\033[35m',
     'c': '\033[36m', }

n = float(input('Insiara um número para que seja calculado seu dobro, tripolo e raiz quadrada:'))

print(str('Número escolhido: {}{}{}'.format(c['c'], n, c['n'])))

op0 = float(n*2)
op1 = float(n*3)
op2 = float(n**(1/2))

print(str('{2}{0}{4} X 2 = {3}{1}{5}'.format
          (n, op0, c['c'], c['r'], c['n'], c['n'])), end='; ')
print(str('{2}{0}{4} X 3 = {3}{1}{4}'.format
          (n, op1, c['c'], c['p'], c['n'], c['n'])), end='; ')
print(str('{2}{0}{4} ^(1/2) = {3}{1:.2f}{5}'.format
          (n, op2, c['c'], c['g'], c['n'], c['n'])))
