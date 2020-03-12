n = int(input('Digite um número [000]-PARAR: '))
continuar = str(input('Quer continuar a digitar valores?[S/N]: ')).upper().strip()[0]

cont = 0
soma = 0
maior = menor = 0

while not n == 000 :
    soma += n
    cont += 1
    media = soma / cont
    n = int(input('Digite um número [000]-PARAR: '))
    continuar = str(input('Quer continuar a digitar valores?[S/N]: ')).upper().strip()[0]
    if  continuar == 's':
        continue
    if continuar == 'n':
        break
    
    if n != 000: #VERIFICANDO O 1 DE TODOS MAIOR e MENOR
        maior = n
        menor = n
    else: #VERIFICANDO O MAIOR EO MENOR
        if n > maior:
            maior = n
        if n < menor:
            menor = n

print('O MAIOR valor lido foi {} e o MENOR {} .'.format(maior,menor))
print('A média de {} valores foi = {:.2f} .'.format(cont,media))