larger = 0
smaller = 999

for i in range(0, 5):
    weight = float(input('Digite um peso em Kg: '))
    if weight > larger:
        larger = weight
    if weight < smaller:
        smaller = weight
print('O maior peso registrado foi de {:.1f}Kg, e o menor foi de {:.1f}Kg'.format(larger, smaller))
