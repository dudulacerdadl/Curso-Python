num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))
num3 = int(input('Digite o terceiro número: '))

smaller = num1
if num2 < num1 and num2 < num3:
    smaller = num2
if num3 < num1 and num3 < num2:
    smaller = num3

larger = num1
if num2 > num1 and num2 > num3:
    larger = num2
if num3 > num1 and num3 > num2:
    larger = num3

print('O maior número indicado é {}, e o menor {}'.format(larger, smaller))
