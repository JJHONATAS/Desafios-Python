maior = 0
menor = 0
for pessoa in range(1,6):
    peso = float(input('Peso da {} ª Pessoa: '.format(pessoa)))

    if pessoa == 1:  #VERIFICANDO O 1 DE TODOS OS PESOS
        maior =  peso
        menor = peso

    else:   #VERIFICANDO MAIOR E MENOR PESO
        if  peso > maior:
            maior = peso
        if peso < menor:
            menor = peso

print('O maior peso lido foi de {:.1f}Kg'.format(maior))
print('O menor peso lido foi de {:.1f}Kg'.format(menor))
