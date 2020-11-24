num = int(input('Digite o valor interio que deseja sacar: R$'))
num2 = num
counter50 = 0
counter20 = 0
counter10 = 0
counter1 = 0

while True:
    if num2 >= 50:
        num2 -= 50
        counter50 += 1
    elif num2 >= 20:
        num2 -= 20
        counter20 += 1
    elif num2 >= 10:
        num2 -= 10
        counter10 += 1
    elif num2 >= 1:
        num2 -= 1
        counter1 += 1
    else:
        break
if counter50 != 0:
    print(f'Foram usadas {counter50} notas de R$50,00')
if counter20 != 0:
    print(f'Foram usadas {counter20} notas de R$20,00')
if counter10 != 0:
    print(f'Foram usadas {counter10} notas de R$10,00')
if counter1 != 0:
    print(f'Foram usadas {counter1} notas de R$1,00')
