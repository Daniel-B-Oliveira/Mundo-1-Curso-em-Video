# 005 - faça um programa que leia um número inteiro e mostre na tela
#       o seu sucessor e seu antecessor

p1 = int(input('Insira um número inteiro: '))

n0 = int(p1 - 1)
n2 = int(p1 + 1)

print(str('\nSequência: {3}{0}{6} ==> {4}{1}{7} ==> {5}{2}{8}'.format
          (n0, p1, n2, '\033[031m', '\033[032m', '\033[033m', '\033[m', '\033[m', '\033[m', )))


