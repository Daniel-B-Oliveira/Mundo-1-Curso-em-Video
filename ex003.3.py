# 007- desenvolva um pragrama que leia as duas notas de um aluno, calcule e mostre a sua média

# Matérias:
#   nt = Notas
#   m1 = matemática
#   m2 = portugûes
#   m3 = história
#   m4 = geográfia
#   m5 = ciências
#   m6 = Ed. Física

c = {'n': '\033[m',
     'r': '\033[31m',
     'g': '\033[32m',
     'y': '\033[33m',
     'b': '\033[34m',
     'p': '\033[35m',
     'c': '\033[36m', }

print(str('Insira as notas'))
m1 = float(input('matemática: '))
m2 = float(input('portugûes: '))
m3 = float(input('história: '))
m4 = float(input('geográfia: '))
m5 = float(input('ciências: '))
m6 = float(input('Ed. Física: '))

mg = float(m1+m2+m3+m4+m5+m6)/6

print('\nMatemática: {6}{0}{12}\nPortuguês: {7}{1}{13}\nHistória: {8}{2}{14}\nGeografia: {9}{3}{15}'
      '\nCiências: {10}{4}{16}\nEd. Física: {11}{5}{17}'
      .format(m1, m2, m3, m4, m5, m6,
              c['r'], c['g'], c['y'], c['b'], c['p'], c['c'],
              c['n'], c['n'], c['n'], c['n'], c['n'], c['n'], ))
print('\n{1}Sua média foi: {3}{2}{0}{4} {5}'
      .format(mg, '\033[7m', '\033[7;41m', c['n'], '\033[7m', c['n']))
