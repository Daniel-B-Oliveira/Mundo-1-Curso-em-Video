# 015 -     Escreva um programa que pergunte a quantidade de Km percorridos
#           por um carro alugado  e a quantidade de dias pelos quais ele foi alugado.
#           Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

senha0 = str(123456)
t0 = float(0.15)  # Valor por Km rodado
t1 = float(0.00)  # Kilometragem inicial
t2 = float(60.0)  # Valor diário do aluguel

senha1 = str(input('Digite a senha se deseja alteral os valores '
                   'ou apens aperte "enter" para prosseguir com estes valores: '))

if senha1 == '':
    print(f'\n!!! \033[31mR${t0}\033[m por Km rodado durante o aluguel !!!'
          f'\n!!! \033[32mR${t2}\033[m por dia de aluguel !!!')
else:
    if senha1 == senha0:
        t0 = float(input('Qual o valor do kilometro rodado? '))
        t2 = float(input('Qual o valor da diária? '))
        p = str(input('Digite (0) se deseja alterar a kilometragem inicial, '
                      'caso contrário apenas aperte "enter" ').strip())
        if p == '0':
            t1 = float(input('Qual a kilometragem inicial do veiculo? '))
            print(f'\n!!! \033[31mR${t0}\033[m por Km rodado durante o aluguel !!!'
                  f'\n!!! \033[32mR${t2}\033[m por dia de aluguel !!!'
                  f'\n!!! \033[33m {t1}Km\033[m: nova kilometragem inicial')
        else:
            print(f'\n!!! \033[31mR${t0}\033[m por Km rodado durante o aluguel !!!'
                  f'\n!!! \033[32mR${t2}\033[m por dia de aluguel !!!')
    else:
        print('\n\033[31mSenha incorreta\033[m')


v0 = int(input('\nPor quantos dias o carro foi alugado? '))
v1 = float(input('\nQual é a kilometragem final do odômetro? '))

print(f'\nValor da kilometragem({float(v1-t1)} km) = \033[34mR${float(t0 * (v1 - t1))}\033[m'
      f'\nValor da diária (R${t2} x {v0} dia) = \033[34mR${float(v0 * t2)}\033[m'
      f'\nValor total a ser pago = \033[34mR$ {float((t0 * (v1 - t1)) + (v0 * t2))}\033[m')
