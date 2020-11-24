num = int(input('Digite o número da tauada desejada: '))

while True:
    for c in range(1, 11):
        print(f'{num} x {c:2} = {num*c}')
    num = int(input('Digite o número da tauada desejada: '))
    if num < 0:
        break
print('Fim')
