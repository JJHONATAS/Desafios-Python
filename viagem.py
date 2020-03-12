distancia = float(input('Qual a Distância da viagem em Km: '))
if distancia <= 200:
    passagem = 0.50 * distancia 
    print('A passagem é de {:.2f} R$'.format(passagem))
else:
    passagem = 0.45 *distancia 
    print('A passagem é de {:.2f} R$'.format(passagem))