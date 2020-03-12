largura = float(input('Qual a Largura da parede em Metros: '))
altura = float(input('Qual a Altura da parede em Metros: '))
area = largura * altura
pintar = area /2
print('você tem uma parede com dimensões {}x{} e sua área é de {}m²'.format(largura,altura,area))
print('para pintar essa parede você precisará de {:.2f}L de tinta'.format(pintar))