num = float(input('Digite um preço: '))
desc = num - (num * (5/100))

print('Seu preço com desconto será: R${:.2f}'.format(desc))
