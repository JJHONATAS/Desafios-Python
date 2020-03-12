print('-='*30)
tupla = ('Flamengo','Santos','Palmeiras','São Paulo','Corinthians','Atlético-MG','Internacional','Bahia','Avaí',
         'Botafogo','Athletico-PR','Goiás','Grêmio','Ceará','Vasco','Fortaleza','Cruzeiro','Chapecoense','Fluminense')

print(f'Lista de times do Brasileirão:{tupla}')
print('-='*30)
print(f'Os 5 primeiros times são:{tupla[0:6]}')
print('-='*30)
print(f'Os 4 últimos são:{tupla[-4:]}')
print('-='*30)
print(f'Os times em ordem alfabética: {sorted(tupla)}')
print('-='*30)
print(f"O Chapecoense está na {tupla.index('Chapecoense')+1} ª posição")