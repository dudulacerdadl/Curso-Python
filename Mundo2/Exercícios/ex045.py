from random import randint
from time import sleep

items = ('Pedra', 'Papel', 'Tesoura')
print('Escolha o que quer usar:')
print('[0] Pedra')
print('[1] Papel')
print('[2] Tesoura\n')

you = int(input('R: '))

if you <= 2:
    print('JO')
    sleep(0.5)
    print('KEN')
    sleep(0.5)
    print('PO!!')
    sleep(0.3)

    print('-=' * 15)
    print('Você escolheu {}'.format(items[you]))
    pc = randint(0, 2)
    print('O computador escolheu {}'.format(items[pc]))
    print('-=' * 15)

    if (pc == 0 and you == 2) or (pc == 1 and you == 0) or (pc == 2 and you == 1):
        print('Você perdeu!')
    elif pc == you:
        print('Empate')
    else:
        print('Você venceu!')
else:
    print('Opção inválida!')
