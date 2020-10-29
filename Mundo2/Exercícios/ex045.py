from random import randint

items = ('Pedra', 'Papel', 'Tesoura')
print('Escolha o que quer usar:\n')
print('[0] Pedra')
print('[1] Papel')
print('[2] Tesoura\n')

you = int(input('R: '))
print('Você escolheu {}'.format(items[you]))
pc = randint(0, 2)
print('O computador escolheu {}'.format(items[pc]))

if (pc == 1 and you == 3) or (pc == 2 and you == 1) or (pc == 3 and you == 2):
    print('Você perdeu!')
elif pc == you:
    print('Empate')
else:
    print('Você venceu!')