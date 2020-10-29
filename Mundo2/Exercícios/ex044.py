price = float(input('Digite o preço do produto: '))
print('Meio de pagamento do produto: ')
print('[1] À vista no dinheiro/cheque')
print('[2] À vista no cartão')
print('[3] 2x no cartão')
print('[4] 3x ou mais no cartão')

payment = int(input('R: '))

if payment == 1:
    print('O valor a ser pago será R${:.2f}'.format(price - (price * 10/100)))
elif payment == 2:
    print('O valor a ser pago será R${:.2f}'.format(price - (price * 5/100)))
elif payment == 3:
    print('Será a compra será feita em 2x de R${:.2f} \nO valor a ser pago será R${:.2f}'.format(price / 2, price))
else:
    price += price * 20/100
    installment = int(input('Digite o número de percelas: '))
    print('''Será a compra será feita em {}x, com juros, pelo valor de R${:.2f} 
O valor total a ser pago será R${:.2f}'''.format(installment, price / installment, price))
