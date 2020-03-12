print('TABUADA V2')
while True:
    n = int(input('Deseja saber a tabuada de multiplicação de qual número? '))
    c = 0      #O MEU CONTADOR TEM QUE ESTAR DENTRO DO LAÇO PARA PODER ATRIBUIR AO OUTRO LAÇO
    print('-'*10)
    while c < 11:
        print(f'{n} x {c} = {n*c}')
        c +=1
    print('-'*10)