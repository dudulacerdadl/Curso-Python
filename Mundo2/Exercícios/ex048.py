sum = 0
counter = 0

for c in range(1, 501, 2):
    if c % 3 == 0:
        sum += c
        counter += 1
print('A soma de todos os {} múltiplos de 3 ímpares entre 1 e 500 é {}'.format(counter, sum))
