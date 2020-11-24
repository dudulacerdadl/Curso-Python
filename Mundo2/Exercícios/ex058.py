from random import randint

counter = 1
pc = randint(0, 10)
print('Estou pensando em um número, consegue adivinhar qual é?\n')
num = int(input('Digite um número: '))

while num != pc:
    print('Não foi dessa vez!')
    if num < pc:
        num = int(input('Tente novamente, e digite um número maior: '))
    else:
        num = int(input('Tente novamente, e digite um número menor: '))
    counter += 1
print('Parabéns!! Você conseguiu!! Você precisou de {} tentativas'.format(counter))
