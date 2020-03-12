s = cont= 0
maior = menor = 0
barato = ' '
while True:
    print('-+='*20,'')
    print('                      MEGA SUPERMERCADO                   ')
    print('-+='*20,'')
    produto = str(input('Nome do Produto: '))
    preco = float(input('Preço: R$ '))
    print('-+='*20,'')
    
    if preco > 1000:  # Se o produto é mais de 1000
        cont +=1

    if cont == 1:       #primeiro preço
        maior = preco
        menor = preco
        barato = produto

    else:
        if preco > maior:   # maior preço
            maior = preco
        if preco < menor:   # menor preço
            menor = preco
            barato = produto

    resp = ' '
    s += preco   # somando os preços dos produtos
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] | ')).strip().upper()[0]
    if resp == 'N':
        break
    
print('-+='*20,'')
print(f'O Total da compra foi R$ {s:.2f}')
print(f'Temos {cont} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {barato} que custa R${menor}')
print(f'O produto mais caro foi R${maior} ')
print('-+='*20,'')
