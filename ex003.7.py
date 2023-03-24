# 011 - Faça um programa que leia a largura e a altura de uma parece em metros,
# calcule a sua área e a quantidade de tinta necessária para pintá-la,
# sabendo que cada litro de tinta pinta uma area de 2m².

r = int(2)
d = float(input('Largura da parede em metros: '))
e = float(input('Altura da parede em metros: '))
p = str(input((f'\nDigite \033[32m0\033[m se deseja alteral o rendimento da tinta \033[31m({r}m²/L)\033[m? ')).strip())
if p != '0':
    pass
else:
    r1 = r
    r = float(input('Qual será o novo rendimento da tinta em metros quadrados (para cada 1 litro)?'))
    print((f'Rendimento alterado de \033[31m{r1}m²/L\033[m para \033[32m{r}m²/L\033[m.'))
rend = (d*e)/r
print(f'\nA quantidade de tinta para pintar \033[36m{e*d}m²\033[m de parede será de \033[36m{rend:.2f}L\033[m.')
