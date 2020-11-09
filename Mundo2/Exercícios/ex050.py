sum = 0
counter = 0

for i in range(0, 6):
    num = int(input('Digite um número: '))
    if num % 2 == 0:
        sum += num
        counter += 1
print('A soma de todos os {} números pares indicados foi de {}'.format(counter, sum))
