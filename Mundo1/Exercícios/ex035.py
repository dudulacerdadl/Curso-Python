r1 = float(input('Digite o primeiro lado do triângulo: '))
r2 = float(input('Digite o segundo lado do triângulo: '))
r3 = float(input('Digite o terceiro lado do triângulo: '))

if r1 > r3 + r2 or r2 > r1 + r3 or r3 > r1 + r2:
    print('Seus lados não podem formar um triângulo!')
else:
    print('Seus lados podem formar um triângulo!')
