from math import hypot

catO = float(input('Comprimento do cateto oposto: '))
catA = float(input('Comprimento do cateto adjacente: '))
hi = hypot(catA, catO)

print('Com um cateto oposto de {} e adjacente de {}, a hipotenusa vai medir {:.2f}'.format(catO, catA, hi))
