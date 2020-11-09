num = int(input('Digite o número da tabuada desejada: '))

for c in range(1, 11):
    print('{} x {:2} = {}'.format(num, c, (num * c)))
