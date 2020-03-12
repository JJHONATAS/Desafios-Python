n = int(input('Digite um número para calcular seu fatorial: '))
f = 1
for c in range(1,n+1):
    print('{} '.format(c), end=' ')
    print(' x ' if c>= 1 else ' = ', end='')
    f *=c
    c -= 1
print('{}'.format(f))