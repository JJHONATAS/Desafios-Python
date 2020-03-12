'''
r = 'S'
while r == 'S':
    n = int(input('Digite um número: '))
    r = str(input('Quer continuar? ')).upper()
print('FIM')
'''
n = 1
par = 0
impar = 0
while n != 0:
    print('[0] Para PARAR')
    n = int(input('Digite um numero: '))
    if n != 0:
        if n % 2 == 0:
            par += 1
        else:
            impar += 1
print('Você digitou {} números pares e {} números ímpares!.'.format(par,impar))