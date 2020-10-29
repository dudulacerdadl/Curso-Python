n1 = int(input('Um valor: '))
n2 = int(input('Outro valor: '))
s = n1 + n2
sub = n1 - n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2

print('A soma vale {}, \n a direfença vale {}, \n o produto vale {}, a divisão vale {:.3f}'.format(s, sub, m, d), end=' ')
print('A divisão inteira é {} e a potência {}'.format(di, e))
