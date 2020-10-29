width = float(input('Digite a largura da parede: '))
height = float(input('Digite a altura da parede: '))
area = width * height
liters = area / 2

print('Serão gastos {}L de trinta para pintar uma área de {}m²'.format(liters, area))
