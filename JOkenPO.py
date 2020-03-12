from random import randint
from time import sleep
itens = ('PEDRA' ,'PAPEL','TESOURA')
computador = randint(0,2)
print('\033[1;31mPEDRA-\033[mPAPEL-\033[1;32mTESOURA')
print('''
    =====OPÇÕES====
      [0] - PEDRA
      [1] - PAPEL
      [2] - TESOURA
    ================
      ''')
jogador = int(input('Digite sua jogada: '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
print('-='*12)
print('COMPUTADOR jogou {}'.format(itens[computador]))
print('JOGADOR jogou {}'.format(itens[jogador]))
print('-='*12)
if computador == 0:  # computador jogou PEDRA
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('JOGADOR VENCE')
    elif jogador == 2:
        print('COMPUTADOR VENCE')
    else:
        print('JOGADA INVÁLIDA')

elif computador == 1:  # computador jogou PAPEL
    if jogador == 0:
        print('COMPUTADOR VENCE')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('JOGADOR VENCE')
    else:
        print('JOGADA INVÁLIDA')

elif computador == 2: # computaor jogou TESOURA
    if jogador == 0:
        print('JOGADOR VENCE')
    elif jogador == 1:
        print('COMPUTADOR VENCE')
    elif jogador == 2:
        print('EMPATE')