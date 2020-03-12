velocidade = int(input('A quantos Km você estava: '))
if velocidade > 80:
    print('Você foi Multado por passar do permitido 80 Km/h !!!')
    multa = 7*(velocidade - 80)
    print('O valor da MULTA é {:.2f} R$'.format(multa))
else:
    print('Tenha um Bom dia!,Dirija com Segurança!!')