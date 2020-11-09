start = int(input('Digite o primeiro número de uma PA: '))
reason = int(input('Digite a razão de uma PA: '))
decimal = start + (10 - 1) * reason
counter = 0

print('')
while counter < 10:
    print(start, end=' -> ')
    start += reason
    counter += 1
print('Acabou')
