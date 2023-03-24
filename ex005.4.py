# 025 - Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.

perg = str('Silva ').title()
name = str(input('Digite seu nome completo: ')).strip().title()

if bool(perg == name) is False:
    print(f'{name} tem Silva? \033[31m{perg in name}\033[m')
else:
    print(f'{name} tem Silva? \033[32m{perg in name}\033[m')
