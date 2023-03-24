# faça um programa que leia algo pelo teclado
# e mostre na tela seu tipo primitivo e todas as informacoes possiveis sovre ele
c = {'n': '\033[m',
     'r': '\033[31m',
     'g': '\033[32m',
     'y': '\033[33m',
     'p': '\033[35m',
     'c': '\033[36m', }

n = input('escreva algo:\n')

print('{}{}{} - type: {}{}{}'.format(c['c'], n, c['n'], c['p'], type(n), c['n']))

# True or False
n01 = bool(n.isascii())
n02 = bool(n.isnumeric())
n03 = bool(n.isalpha())
n04 = bool(n.isalnum())
n05 = bool(n.isdigit())
n06 = bool(n.isdecimal())
n07 = bool(n.isidentifier())
n08 = bool(n.islower())
n09 = bool(n.isupper())
n10 = bool(n.istitle())
n11 = bool(n.isspace())
n12 = bool(n.isprintable())

print('Is {}ASCII{} -'.format(c['c'], c['n']), end=' ')
print('{}Verdadeiro{}'.format(c['g'], c['n'])) if n01 is True else print('{}falso{}'.format(c['r'], c['n']))

print('Is {}numeric{} -'.format(c['c'], c['n']), end=' ')
print('{}Verdadeiro{}'.format(c['g'], c['n'])) if n02 is True else print('{}falso{}'.format(c['r'], c['n']))

print('Is {}alpha{} -'.format(c['c'], c['n']), end=' ')
print('{}Verdadeiro{}'.format(c['g'], c['n'])) if n03 is True else print('{}falso{}'.format(c['r'], c['n']))

print('Is {}alnum{} -'.format(c['c'], c['n']), end=' ')
print('{}Verdadeiro{}'.format(c['g'], c['n'])) if n04 is True else print('{}falso{}'.format(c['r'], c['n']))

print('Is {}digit{} -'.format(c['c'], c['n']), end=' ')
print('{}Verdadeiro{}'.format(c['g'], c['n'])) if n05 is True else print('{}falso{}'.format(c['r'], c['n']))

print('Is {}decimal{} -'.format(c['c'], c['n']), end=' ')
print('{}Verdadeiro{}'.format(c['g'], c['n'])) if n06 is True else print('{}falso{}'.format(c['r'], c['n']))

print('Is {}identifier{} -'.format(c['c'], c['n']), end=' ')
print('{}Verdadeiro{}'.format(c['g'], c['n'])) if n07 is True else print('{}falso{}'.format(c['r'], c['n']))

print('Is {}lower{} -'.format(c['c'], c['n']), end=' ')
print('{}Verdadeiro{}'.format(c['g'], c['n'])) if n08 is True else print('{}falso{}'.format(c['r'], c['n']))

print('Is {}upper{} -'.format(c['c'], c['n']), end=' ')
print('{}Verdadeiro{}'.format(c['g'], c['n'])) if n09 is True else print('{}falso{}'.format(c['r'], c['n']))

print('Is {}title{} -'.format(c['c'], c['n']), end=' ')
print('{}Verdadeiro{}'.format(c['g'], c['n'])) if n10 is True else print('{}falso{}'.format(c['r'], c['n']))

print('Is {}space{} -'.format(c['c'], c['n']), end=' ')
print('{}Verdadeiro{}'.format(c['g'], c['n'])) if n11 is True else print('{}falso{}'.format(c['r'], c['n']))

print('Is {}printable{} -'.format(c['c'], c['n']), end=' ')
print('{}Verdadeiro{}'.format(c['g'], c['n'])) if n12 is True else print('{}falso{}'.format(c['r'], c['n']))
