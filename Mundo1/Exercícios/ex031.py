distance = float(input('Digite a distância da viagem: '))

if distance < 200:
    value = distance * 0.5
else:
    value = distance * 0.45

print('O valor da viagem será de R${:.2f}'.format(value))
