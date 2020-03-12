play = False
while not play:
    n1 = int(input('Primeiro valor: '))
    n2 = int(input('Segundo valor: '))
    print('''
          [1] - Para SOMAR
          [2] - Para MULTIPLICAR
          [3] - Para o MAIOR
          [4] - Novos NÚMEROS
          [5] - SAIR
          ''')
    opcao= int(input('>>'))
    if opcao == 1:
        soma = n1 + n1
        print('A SOMA de {} + {} = {}'.format(n1,n2,soma))
        break
    elif opcao == 2:
        multiplicar = n1 * n2
        print('A MULTIPLICAÇÃO de {} x {} = {}'.format(n1,n2,multiplicar))
        break
    elif opcao == 3:
        if n1> n2:
            print('O maior é {}'.format(n1))
        else:
            print('O maior é {}'.format(n2))
        break
    if opcao == 4:
        novos_numeros = play
    if opcao == 5:
        print('EXIT')
        break