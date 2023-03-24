# 027 - Faça um programa que leia o nome completo de uma pessoa,
#       mostrando em seguida o primeiro e o último nome separadamente.

name = str(input('Escrava um nome completo: ')).strip().split()

print(str(f'\nPrimeiro nome: \033[35m{name[0]}\033[m\nÚltimo nome: \033[34m{name[len(name)-1]}\033[m'))
