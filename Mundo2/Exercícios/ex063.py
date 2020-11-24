start = 1  # int(input('Digite o número inicial: '))
repeat = int(input('Digite a quantidade de números desejados: '))
counter = 0
previous = 0

while counter < repeat:
    print('{}'.format(previous), end=' -> ')
    start += previous
    print('{}'.format(start), end=' -> ')
    previous += start
    counter += 2
print('FIM')
