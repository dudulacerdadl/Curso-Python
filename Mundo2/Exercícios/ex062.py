start = int(input('Digite o primeiro número de uma PA: '))
reason = int(input('Digite a razão de uma PA: '))
decimal = start + (10 - 1) * reason
counter = 0
terms = 10

print('')
while terms != 0:
    while counter < terms:
        print(start, end=' -> ')
        start += reason
        counter += 1
    counter = 0
    terms = int(input('Deseja escrever mais quantos termos: '))
print('Acabou')
