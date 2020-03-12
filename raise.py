def mes(n):
    meses = [
        'Janeiro',
        'Fevereiro',
        'Março',
        'Abril',
        'Maio',
        'Junho',
        'Julho',
        'Agosto',
        'Setembro',
        'Outubro',
        'Novembro',
        'Dezembro'
    ]
    try:
        return meses[n-1]
    except:
        raise Exception('Mês Inválido')
print(mes(12))
print(mes(24))