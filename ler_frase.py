frase = str(input('Qual a sua Frase marcante? ')).upper().strip()
print('Quantas vezes aparece a letra "a": {} '.format(frase.count('A')))
print('Na primeira vez aparece na posição: {}'.format(frase.find('A')+1))
print('A última letra "a" apareceu na posição:{}'.format(frase.rfind('A')+1))