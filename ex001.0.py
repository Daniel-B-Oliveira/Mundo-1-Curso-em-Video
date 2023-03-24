# nome = input('Qual é o seu nome?')
# idade = input('Qual é a sua idade '+nome+'?')
# altura = input('Qual a sua altura '+nome+'?')
# peso = input('Qual o seu peso '+nome+'?')
# print('nome: '+nome+' idade: '+idade+' altura: '+altura+' peso: '+peso)
# print('seu nome é', nome+' sua idade é', idade+' sual atura é', altura+' seu peso é', peso)

c = {'n': '\033[m',
     'r': '\033[31m',
     'g': '\033[32m',
     'y': '\033[33m',
     'p': '\033[35m',
     'c': '\033[36m', }

nome = str(input('Qual é o seu nome? ')).strip().title()

sexo = int(input('{}{}{}, Digite {}0{} se seu corpo for do sexo masculino, Digite {}1{} se for feminino: '
                 .format(c['c'], nome, c['n'], c['p'], c['n'], c['p'], c['n'])))
if sexo != 0 and sexo != 1:
    print('\033[31mVariável inaceitável, o programa apresentará erros, tente reinicia-lo.\033[m')

altura = int(input('Qual a sua altura em centimentros? '))

peso0 = float(input('Qual o seu peso {}{}{}? '.format(c['c'], nome, c['n'])))

peso1 = float(altura-100)*0.90  # Calcula o peso 'ideal'
sexo0 = 'um homem'

if sexo == 1:
    peso1 = float(altura-100)*0.85
    sexo0 = 'uma mulher'

peso2 = float(peso0/peso1)  # Calcula a distância do peso atual para o 'ideal'
peso3 = peso2/100
if peso2 > 1:
    peso3 = (peso2 - 1) * 100
if peso2 < 1:
    peso3 = (1 - peso2)*100
r = '{}{}{}, seu peso é de {}{}{}, sendo próximo de {}{:.2f}%{} do peso ideal'\
    .format(c['c'], nome, c['n'], c['g'], peso0, c['n'], c['g'], peso3, c['n'])

if 0 < peso0 < (peso1*0.75):  # Se a pessoa tiver o peso menor
    if peso2 < 0.5:
        r = '{}{}{}, seu peso é de {}{}{}, abaixo em {}{:.2f}%{} do peso ideal'\
            .format(c['c'], nome, c['n'], c['y'], peso0, c['n'], c['y'], peso3, c['n'])
    else:
        r = '{}{}{}, seu peso é de {}{}{}, abaixo em {}{:.2f}%{} do peso ideal' \
            .format(c['c'], nome, c['n'], c['r'], peso0, c['n'], c['r'], peso3, c['n'])

if 1 < peso0 > (peso1*1.25):  # Se a pessoa tiver o peso menor
    if peso2 > 1.5:
        r = '{}{}{}, seu peso é de {}{}{}, acima em {}{:.2f}%{} do peso ideal'\
            .format(c['c'], nome, c['n'], c['r'], peso0, c['n'], c['r'], peso3, c['n'])
    else:
        r = '{}{}{}, seu peso é de {}{}{}, acima em {}{:.2f}%{} do peso ideal' \
            .format(c['c'], nome, c['n'], c['y'], peso0, c['n'], c['y'], peso3, c['n'])


print(r, end='')
print('({}{}Kg{}).\n'.format(c['p'], peso1, c['n']))
print('\033[31mEste programa é meramente um exercício, não sendo recomendado seu uso clínico =)')
