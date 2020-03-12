listagem = ('Lápis',1.75,
            'Borracha',2.00,
            'Caderno' , 15.90,
            'Estojo' , 25.00,
            'Livro' , 34.90,
            'Transferidor' , 4.20,
            'Compasso' , 9.99,
            'Mochila' , 120.32,
            'Canetas' , 22.30)

print('_'*45)
print(f'{"LISTAGEM DE PREÇOS":^40}')                # CENTRALIZANDO COM 40 ESPAÇOS
print('_'*45)

for pos in range(0,len(listagem)):
    if pos % 2 == 0:           # SE FOR PAR É UM NOME DE UM PRODUTO
        print(f'{listagem[pos]:.<30}', end= ' ')           #    .<30 AQUI ELE ALINHA A ESQUERDA COM 30 ESPAÇOS E CHEIO DE PONTINHOS NA MESMA LINHA
    else:                               # SE FOR IMPAR É UM PREÇO DO PRODUTO
        print(f'R${listagem[pos]:>7.2f}')                  # :>10.2f ALINHANDO A DIREITA COM 7 ESPAÇOS E COM FORMATAÇÃO DE 2 CASA FLUTUANTE

print('_'*45)