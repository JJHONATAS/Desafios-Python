tupla = ('Zero','Um','Dois','Três','Quatro',
         'Cinco','Seis','Sete','Oito','Nove','Dez',
         'Onze','Doze','Treze','Quatorze','Quinze',
         'Dezesseis','Dezessete','Dezoito','Dezenove','Vinte')

while True:
    n = int(input('Número emtre 0 e 20: '))
    if 0 <= n <= 20:
        break
    print('Tente novamente...', end=' ')

print(f'você digitou o número {tupla[n]}')





