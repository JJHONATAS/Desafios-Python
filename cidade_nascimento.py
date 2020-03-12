cidade = str(input('Em qual cidade você nasceu? ')).strip()
print('Vamos ver se você nasceu em alguma cidade com palavra inicial SANTO!')
print(cidade[:5].upper() == 'SANTO')