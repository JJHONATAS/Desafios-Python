
#PARANDO COM CONTAGEM DE 5 VEZES
n = s = cont = 0
while cont <= 5:
    n = int(input('Digite um número: '))
    cont +=1
    s += n
print(f'Você contou {cont} vezes e seu somatório foi {s}')

#PARANDO SE n == 999
n = s = 0
while True :
    n = int(input('Digite um número: '))
    if n == 999:
        break
    
    s += n
print(f'O Somatório  de n é {s}')

#CONTANDO ATÉ 10
cont = 1
while cont <= 10:
    print(cont,' ...', end=' ')
    cont +=1
print('Acabou!')
