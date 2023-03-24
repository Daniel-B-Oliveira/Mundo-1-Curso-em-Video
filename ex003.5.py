# 009 - Faça um programa que leia um número inteiro qualquer e mostre na tela a sua tabuada

c = {'n': '\033[m',
     'w': '\033[30m',
     'r': '\033[31m',
     'g': '\033[32m',
     'y': '\033[33m',
     'b': '\033[34m',
     'p': '\033[35m',
     'c': '\033[36m',
     's': '\033[37m', }

n = int(input('Coloque um valor inteiro: '))

print('{2}{0}{5} X {3}1{6} = {4}{1}{7}'.format(n, n*1, c['s'], c['r'], c['p'], c['n'], c['n'], c['n']))
print('{2}{0}{5} X {3}2{6} = {4}{1}{7}'.format(n, n*2, c['s'], c['g'], c['p'], c['n'], c['n'], c['n']))
print('{2}{0}{5} X {3}3{6} = {4}{1}{7}'.format(n, n*3, c['s'], c['y'], c['p'], c['n'], c['n'], c['n']))
print('{2}{0}{5} X {3}4{6} = {4}{1}{7}'.format(n, n*4, c['s'], c['b'], c['p'], c['n'], c['n'], c['n']))
print('{2}{0}{5} X {3}5{6} = {4}{1}{7}'.format(n, n*5, c['s'], c['p'], c['p'], c['n'], c['n'], c['n']))
print('{2}{0}{5} X {3}6{6} = {4}{1}{7}'.format(n, n*6, c['s'], c['c'], c['p'], c['n'], c['n'], c['n']))
print('{2}{0}{5} X {3}7{6} = {4}{1}{7}'.format(n, n*7, c['s'], c['r'], c['p'], c['n'], c['n'], c['n']))
print('{2}{0}{5} X {3}8{6} = {4}{1}{7}'.format(n, n*8, c['s'], c['g'], c['p'], c['n'], c['n'], c['n']))
print('{2}{0}{5} X {3}9{6} = {4}{1}{7}'.format(n, n*9, c['s'], c['y'], c['p'], c['n'], c['n'], c['n']))
print('{2}{0}{5} X {3}10{6} = {4}{1}{7}'.format(n, n*10, c['s'], c['p'], c['p'], c['n'], c['n'], c['n']))

