# #09 - Manipulando Texto

# Print("""???"""): exibi os texto exatamente como está digitado, incluindo quebra de linhas

# frase = srt('Testo para texte')

# frase[a:b:c]
# a: posição do caracter inicial da frase, se vazio igual a 0
# b: posição do caracter final + 1, se vazio igual a ultimo caracter
# c: número de casas que será pulada de contagem em contagem

# <<<<ANÁLISE:>>>>
# len(frase): comprimento da frase
# frase.count('?'): conta o número de vezes que aparece o caracter selecionado
# frase.count('?', x, y): ádiciona a opcão do fatiamento da frase (inicio e fim)
# frase.find('???'): encontra a casa inicial do intervalo mencionado, se a frase não existir nesse intervalo
#                                                                       valor = -1
# '???' in frase: verifica se o intervalo pesquisado existe na variável selecionada

# <<<<TRANSFORMAÇÃO>>>>
# frase.replace('a', 'b'): troca o intervalo(s) 'a' por 'b' (troca não efetuada na variável principal)
# frase.upper(): transformar os caracteres possiveis em maiúsculo, casa já não sejam
# frase.lowe(): inverso de upper
# frase.captalize(): mesmo efeito de lower + transforma o primeiro caracter necessariamente em maiúsculo
# frase.title(): mesmo efeito de captalize + maiúcula todos os caracters iniciais após espaço: (' ')
# frase.strip(): elimina os espaços: (' ') inuteis no começo e final de cada string
# frase.rstrip(): [rstrip = r(righ) + strip]
#           mesmo efeito de strip mas remove os espaços
#            apenas do final(r) ou inicio(l) da string
# frase.lstrip(): [lstrio = l()left + strip]

# <<<<DIVSÃO>>>>
# frase.split(): dividi onde possuir espaço: (' ') --> TRANSFORMA DE STR PARA LISTA

# <<<<JUNÇÃO>>>>
# 'x'.join(frase): junta todos os elementos em que as frases foram divididas com a str('x') desejada

fra = str('flor linda flor linda alegria linda.')
div = fra.split()
print(div[2][3])
