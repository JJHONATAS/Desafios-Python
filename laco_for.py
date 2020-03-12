#Entendendo o FOR
i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
for c in range(i,f+1,p):
    print(c)
print('END')

#PEDINDO UMA ENTRA 5x e SOMANDO-O SEUS VALORES
s = 0
for c in range(0,5):
    n = int(input('Digite um valor: '))
    s += n
print('O somatório de todos os valores é {}'.format(s))
