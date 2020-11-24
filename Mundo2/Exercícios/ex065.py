counter = 0
sum = 0
up = 0
down = 0
option = ''

while option != 'N':
    num = int(input('Digite um número: '))
    sum += num
    if counter == 0:
        up = num
        down = num
    if num > up:
        up = num
    if num < down:
        down = num
    counter += 1
    option = input('Deseja continuar? [S/N]: ').upper()
    if option not in 'NS':
        option = input('Digite uma opção válida! [S/N]: ').upper()
media = sum / counter
print('Fora digitados {} números, tento uma soma de {} números, com uma média de {}, tendo {} como menor número e {} como maior'. format(counter, sum, media, down, up))
