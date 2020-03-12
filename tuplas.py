# TUPLAS SÃO IMÚTAVEIS

lanche = ('Hambúrger', 'Suco','Pizza','Pudim')

print(len(lanche))   #QNT DE ELEMEnTOS DE LANCHE
print(sorted(lanche))    #MOSTRANDO OS LANCHES EM ORDEM

for comida in lanche:
    print(f'Eu vou comer {comida}')


for cont in range(0,len(lanche)):
    print(f'Eu vou comer {lanche[cont]} na posição {cont}')

for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}')

print('Comi pra CARAMBA!')

a = (2,5,4)
b = (8,5,2)
c = b + a
print(c) # ELE CONCATENA OS ELEMENTOS
print(c.count(5))    # mostra quantos valores aparece
print(c.index(8)) # mostrando a posição do índice