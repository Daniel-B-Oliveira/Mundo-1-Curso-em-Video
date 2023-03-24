#  024 - Crie um programa que leia o nome de uma cidade diga
#        se ela começa ou não com o nome "SANTO"

namecid0 = str('Santo')
name0 = (input('Digite o nome de uma cidade').strip().title())

ver0 = (namecid0.strip().title()) + " " in str((name0.split()[0]) + " ")
ver1 = namecid0.lower() in str((name0.lower().split()[0])).lower()

if ver0 is False:
    ver0 = f'\033[31m{ver0}\033[m'
else:
    ver0 = f'\033[32m{ver0}\033[m'

if ver1 is False:
    ver1 = f'\033[31m{ver1}\033[m'
else:
    ver1 = f'\033[32m{ver1}\033[m'

namecid0 = f'\033[36m{namecid0}\033[m'
name0 = f'\033[36m{name0}\033[m'

print(f'\nA cidade "{name0}" começa com "{namecid0}"?\n{ver0}'
      f'\n\n"{namecid0.lower()}" está entre "{name0.strip().split()[0]}"?\n{ver1}')
