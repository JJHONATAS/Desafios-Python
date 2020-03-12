print('\033[1m ===MAIOR NÚMERO===')
n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
if n1 > n2:
    print('{} o primeiro valor é MAIOR'.format(n1))
elif n2 > n1:
    print('{} o segundo valor é MAIOR'.format(n2))
else:
    print('Não existe valor maior, os dois são iguais n1{} n2 {}'.format(n1,n2))