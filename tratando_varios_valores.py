n = cont = soma = 0
n = int(input('DIgite um número [999] - para parar: '))
while n != 999:
    cont+= 1
    soma += n
    n = int(input('DIgite um número [999] - para parar: '))
print('Você digitou {} números e a soma entre eles foi {}'.format(cont,soma))