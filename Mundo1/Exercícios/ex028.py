from random import randint
from time import sleep

print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5, tente adicinhar:  ')
print('-=-' * 20)

num = int(input('R: '))
numSort = randint(0, 5)

print('Processando...')
sleep(2)

if num == numSort:
    print('Você venceu, Parabéns!')
else:
    print('Você perdeu, pensei em {} não {}. Tente novamente!'.format(numSort, num))
