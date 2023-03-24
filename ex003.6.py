# 010 - Crie um programa que leia quanto dinheiro uma pessoa tem na carteira
# e mostre quantos dólares ela pode comprar
v = float(5.22)
p = str(input('Digite \033[31m[0]\033[m se deseja mudar o valor do dólar em raal \033[32m({})\033[m,'
              ' caso contrário aperta qualquer outra tecla. '
              .format(v)).strip())
if p == '0':
    p = v
    v = float(input('Qual o valor atual do \033[31mdolar\033[m? '))
    print('Valor alternado de {} para {}.'.format(p, v))

s = float(input('Qual o valor do seu \033[32msaldo\033[m? '))
spv = float(s/v)

print('\nSeu saldo em \033[033mreal\033[m: \033[33mR${:.2f}\033[m'.format(s))
print('Seu saldo em \033[031mdolar\033[m: \033[31mUS${:.3f}\033[m'.format(spv))
