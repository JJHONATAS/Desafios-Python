from random import randint
computador = randint(0,10)
print('Sou o Computador... Acabei de pensar em um número entre e 0 e 10.')
print('Será que você consegue advinhar qual foi?')
acertou = False
palpites = 0
while not acertou:
    usuario = int(input('Qual seu palpite? '))
    palpites +=1
    if usuario == computador:
        acertou = True
    else:
        if usuario < computador:
            print('Mais... Tente mais uma vez!')
        else:
            print('Menos... Tente mais uma vez!')
            
print('Acertou com {} tentativas.!'.format(palpites))