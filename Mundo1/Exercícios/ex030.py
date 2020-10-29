num = int(input('Digite um número: '))
isOdd = num % 2

if isOdd == 1:
    print('O número {} é ímpar'.format(num))
else:
    print('O número {} é par'.format(num))
