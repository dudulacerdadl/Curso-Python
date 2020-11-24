cheap = ''
cheapPrice = 0
finalPrice = 0
counter = 0

while True:
    name = input('Digite o nome do produto: ')
    price = float(input('Digite o preço do produto: '))
    finalPrice += price
    if price > 1000:
        counter += 1
    if cheapPrice > price or cheapPrice == 0:
        cheap = name
        cheapPrice = price
    option = input('Deseja continuar [S/N]: ').upper()
    while option != 'S' and option != 'N':
        option = input('Digite uma opção válida! [S/N]: ').upper()
    if option == 'N':
        break
print(f'Foram gastos R${finalPrice:.2f} nessa compra.\n'
      f'{counter} produtos comprados custavam mais de R$1.000,00.\n'
      f'{cheap} foi o produto mais barato comprado, custando apenas R${cheapPrice:.2f}')
