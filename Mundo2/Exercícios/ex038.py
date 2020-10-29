num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))

if num1 > num2:
    print('{} é maior do que {}'.format(num1, num2))
elif num1 < num2:
    print('{} é maior do que {}'.format(num2, num1))
else:
    print('Os números {} e {} são iguais'.format(num1, num2))
