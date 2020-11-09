counter = -1
sum = 0 - 999
num = 0

while num != 999:
    num = int(input('Digite um número: '))
    sum += num
    counter += 1
print('Foram digitados {} números, e a soma deles é {}'.format(counter, sum))
