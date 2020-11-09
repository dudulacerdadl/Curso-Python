start = int(input('Digite o primeiro número de uma PA: '))
reason = int(input('Digite a razão de uma PA: '))
decimal = start + (10 - 1) * reason

for i in range(start, decimal, reason):
    print(i, end=' -> ')
print('Acabou')
