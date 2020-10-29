num = int(input('Digite um número: '))
double = num * 2
triple = num * 3
# square = num ** (1/2)
square = pow(num, (1 / 2))

print('O número digitado foi {} \nSeu dobro é {} \nSeu triplo é {} \nSua raiz quadrada é {:.2f}'.format(num, double, triple, square))
