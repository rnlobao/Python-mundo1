largura = float(input('Digite a largura da parede: '))
altura = float(input('Digite a altura da parede: '))
area = altura * largura
litrodetinta = area / 2
print('Litros de tinta necessarios: {} para {} metros quadrados'.format(litrodetinta, area))
