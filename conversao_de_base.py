print(' CONVERSOR DE BASE ')
numero = int(input('Digite o número para converter: >> '))
n = int(input('  [1] BINÁRIO  [2] OCTAL [3] HEXADECIMAL : >> '))
if n == 1:
    print('{} convertido para BINÁRIO é {} '.format(numero, bin(numero) [2:] ))
elif n == 2:
    print('{} convertido para OCTAL é {} '.format(numero, oct(numero) [2:] ))
elif n == 3:
     print('{} convertido para HEXADECIMAL é {} '.format(numero, hex(numero) [2:] ))
else:
    print('ENTRADA INVÁLIDA')
