num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))
option = 0

while option != 5:
    print('O que deseja fazer?\n')
    print('[1] Somar\n[2] Multiplicar\n[3] Maior\n[4] Novos números\n[5] Sair')
    option = int(input('R: '))

    if option == 1:
        res = num1 + num2
        print('A soma de {} e {} é {}'.format(num1, num2, res))
    elif option == 2:
        res = num1 * num2
        print('A multiplicação de {} e {} é {}'.format(num1, num2, res))
    elif option == 3:
        if num1 == num2:
            print('{} e {} são iguais'.format(num1, num2))
        elif num1 > num2:
            print('{} é maior que {}'.format(num1, num2))
        else:
            print('{} é maior que {}'.format(num2, num1))
    elif option == 4:
        num1 = int(input('Digite o primeiro número novamente: '))
        num2 = int(input('Digite o segundo número novamente: '))
    elif option != 5:
        print('Digite um opção válida!')

print('Muito obrigado por usar nosso sistema!')
