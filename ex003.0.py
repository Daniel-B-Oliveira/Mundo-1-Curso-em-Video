# (+) adi.
# (-) sub.
# (*) mul.
# (/) div.
# (**) pot.
# (//) div. int.
# (%) res. div.


# nome = input('Qual é o seu nome?')
# print('prazer em te conhecer {:=^20}!'.format(nome))
# {:n} -> {:[?]n} -> {:[<,=,>]n}

space = str('\033[32m=\033[m' * 100)
c = {'n': '\033[m',
     'r': '\033[31m',
     'g': '\033[32m',
     'y': '\033[33m',
     'p': '\033[35m',
     'c': '\033[36m', }

print(space)

n1 = float(input('\nColoque um número: '))
n2 = float(input('Coloque outro número: '))

adi = float(n1 + n2)
sub = float(n1 - n2)
mul = float(n1 * n2)
div = float(n1 / n2)
pot = float(n1 ** n2)
divint = float(n1 // n2)
resdiv = float(n1 % n2)

print('\n'+space)

# m2 = ('adi = {} ; sub = {} ; \nmul = {} ; pot = {:.4}'.format(adi, sub, mul, pot))
# m3 = ('div = {:.3f} ; \ndiv (int) = {} ; rest = {}'.format(div, divint, resdiv))

print('\nadi = {4}{0}{8} ; sub = {5}{1}{9} ; mul = {6}{2}{10} ; pot = {7}{3}{11}'.format
      (adi, sub, mul, pot, c['r'], c['g'], c['c'], c['p'], c['n'], c['n'], c['n'], c['n']))
print('div = {3}{0:.3f}{6} ; div (int) = {4}{1}{7} ; rest = {5}{2}{8}\n'.format
      (div, divint, resdiv, c['y'], c['y'], c['y'], c['n'], c['n'], c['n']))

print(space)
