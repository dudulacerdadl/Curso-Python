days = int(input('Dias alugados: '))
km = float(input('Quilometros percorridos: '))
value = (60 * days) + (0.15 * km)

print('O valor a pagar é R${:.2f}'.format(value))
