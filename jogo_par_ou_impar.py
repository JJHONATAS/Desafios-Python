from random import randint
print('-=+'*10)
print('JOGO PAR OU ÍMPAR')
print('-=+'*10)

v = 0 # VARIÁVEL DE VITÓRIAS
while True:
    jogador = int(input('Diga um valor: '))
    computador = randint(0,100)
    total = jogador + computador #TOTAL DO PAR OU ÍMPAR
    tipo = ' '
    while tipo not in 'PI': # ESCOLHA PARA PAR OU PARA ÍMPAR
        tipo = str(input('Par ou Ímpar? [P/I] | ')).strip().upper()[0]
    print(f'Você jogou {jogador} e o computador {computador}. Total de {total} ', end=' ')
    print('DEU PAR' if total % 2 == 0 else 'DEU ÍMPAR') # VERIFICANDO SE DEU PAR OU IMPAR NO FINAL NA LINHA ACIMA
    if tipo =='P': # VERIFICANDO SE MEU TIPO É PAR
        if total  % 2 == 0:
            print('Você VENCEU!')
            v +=1
        else:
            print('Você PERDEU!')
            break
    elif tipo == 'I': # VERIFICANDO SE MEU TIPO É ÍMPAR
        if total % 2 == 1:
            print('Você VENCEU!')
            v +=1
        else:
            print('Você PERDEU!')
            break
    print('Vamos Jogar Novamente...')
print(f'GAME OVER ! Você venceu {v} vezes.')