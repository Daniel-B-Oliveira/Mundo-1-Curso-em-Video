# #11 - Cores no Terminal
# ANSI: escape sequence
# \033[?,?,?m
# ?,?,? = a;b;c
# a: style; ex: itálico
#       0: None
#       1: Bold
#       4: Underline
#       7: Negative (troca b por c)
# b: text; cor do texto
#       cores de 30->37
#           branco
#           vermelho
#           verde
#           azul
#           amarelo
#           azul
#           magente
#           ciano
#           cinza
# c: back; cor de fundo
#       cores de 40->47

color = str('\033[32m')
ncolor = str('\033[m')

# DICIONÁRIO!!!
cores = {'nada': '\033[m',
         'vermelha': '\033[31m',
         'roxa': '\033[35m'}

men = str(input('Escreva uma mensagem de bom dia: '))

print(f'Está é sua mensagem: "\033[35m{men}\033[m".\nQue mensagem \033[31mlinda\033[m!!!')
