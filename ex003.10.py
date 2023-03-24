# 014 Escreva um programa que converta uma temperatura digitando em graus Celsius
# e converta para graus Fahrenheit.

C = float(input("Coloque uma temperatura em centigrados"))
print(f'\033[31m{C}C°\033[m = \033[32m{C*1.8+32:.1f}°F\033[m e \033[33m{C+273.15:.2f} K\033[m')
