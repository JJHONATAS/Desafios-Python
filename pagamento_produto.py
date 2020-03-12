print('{:=^40}'.format(' LOJAS LUCIA '))
preço = float(input('Qual o  preço do produto?R$ '))
print('''
      [FORMAS DE PAGAMENTO]
      [1] - À VISTA: DINHEIRO/CHEQUE; 10% DE DESCONTO
      [2] - À VISTA: CARTÃO; 5% DE DESCONTO
      [3] - NORMAL: 2x NO CARTÃO/SEM JUROS
      [4] - NORMAL: 3x NO CARTÃO OU MAIS/20% DE JUROS
      ''')
opcao = int(input('>> '))
if opcao == 1:
    total =  preço - (preço * 10/100)
    
elif opcao == 2:
    total = preço - (preço * 5/100)

elif opcao == 3:
    total = preço
    parcela= preço / 2
    print('Sua compra será parcelada em 2x de R$ {:.2f}'.format(parcela))

elif opcao == 4:
    total = preço + (preço*20/100)
    totalparcelas = int(input('Quantas parcelas: '))
    parcela = total / totalparcelas
    print('Sua compra será parcelada em {}x de R${:.2f} COM JUROS.'.format(totalparcelas,parcela))

else:
    total = 0
    print('\033[1;31m Opção Inválida,Tente novamente!')
print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(preço,total))