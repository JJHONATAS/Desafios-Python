print('VERIFICAR SE A FRASE É UM PALÍNDROMO')
frase = str(input('Qual sua Frase? ')).strip().upper()
palavras = frase.split()
junto = ' '.join(palavras)
inverso = junto[::-1]   #USANDO FATIAMENTO DE STRING
#USANDO COM LAÇO
'''
inverso = ' '
for letra in range(len(junto) - 1, -1 , -1):
    inverso += junto[letra]
'''
print('O inverso de {} é {}'.format(junto,inverso))
if inverso == junto:
    print('Temos um palíndromo!')
else:
    print('A frase digitada não é um palíndromo.')