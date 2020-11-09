num = int(input('Digite um número: '))
counter = 0

for i in range(1, num+1):
    if num % i != 0:
        print('\033[0;31m{}\033[m'.format(i), end=' ')
    else:
        print('\033[0;33m{}\033[m'.format(i), end=' ')
        counter += 1
print('\nO número foi divisível {} vezes'.format(counter))

if counter > 2:
    print('O número escrito NÃO é primo')
else:
    print('O número escrito é primo')
