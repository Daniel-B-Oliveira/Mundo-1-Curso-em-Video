# 018 -     Faça um programa que leia um ângulo qualquer e mostre na tela o valor
#           do seno, cosseno e tangente desse ângulo

from math import radians, sin, cos, tan
from greek import π
from fractions import Fraction

ang = float(input('Valor do ângulo: '))

print(f'\n{ang}º em radianos = \033[36m{Fraction((radians(ang))/π).limit_denominator(100)} π\033[m rad '
      f'ou \033[36m{(radians(ang))/π:.3f} π\033[m rad'
      f'\n\nSeno de {ang}° = \033[31m{sin(radians(ang)):.4f}\033[m'
      f'\nCosseno de {ang}° = \033[32m{cos(radians(ang)):.4f}\033[m'
      f'\nTangente de {ang}° = \033[33m{tan(radians(ang)):.4f}\033[m')
