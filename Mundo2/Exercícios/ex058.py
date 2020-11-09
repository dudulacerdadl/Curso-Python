from random import randint

counter = 1
pc = randint(0, 10)
print(pc)
print('Estou pensando em um número, consegue adivinhar qual é?\n')
num = int(input('Digite um número: '))

while num != pc:
    print('Não foi dessa vez!')
    num = int(input('Tente novamente: '))
    counter += 1
print('Parabéns!! Você conseguiu!! Você precisou de {} tentativas'.format(counter))
