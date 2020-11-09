num = int(input('Digite um número: '))
num2 = num
counter = num - 1

while counter > 0:
    num2 *= counter
    counter -= 1
print('{}! = {}'.format(num, num2))
