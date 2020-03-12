print('='*30)
print('{:^30}'.format('BANCO DO MONEY'))
print('='*30)

valor = int(input('Que valor você quer sacar? R$ '))
montante = valor
cédula = 50
total_cédula = 0
while True:
    if montante >= cédula:  # SE EU PUDER TIRAR 50 DESSE VALOR
        montante -= cédula
        total_cédula += 1
    else:
        if total_cédula > 0: # SE O TOTAL DAS CÉDULAS FOR MAIOR QUE ZERO
            print(f'Total de {total_cédula} cédulas de R$ {cédula}')
        if cédula == 50:   # Não conseguir tirar 50
            cédula = 20      # Agora tento tirar 20
        elif cédula == 20:
            cédula = 10      # Agora tento tirar 10
        elif cédula == 10:
            cédula = 1        # Agora tento tirar 1
        total_cédula = 0  # A CADA VEZ QUE MUDAR A NOTA, TEM QUE FAZER A CÉDULA VOLTAR A ZERO
        if montante == 0:  # SE A CONTAGEM ACABAR ELE PARA
            break
print('='*30)
print('Volte sempre ao BANCO MONEY!')
