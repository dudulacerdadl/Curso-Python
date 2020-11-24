from random import randint

counter = 0
while True:
    comp = randint(0, 100)
    num = int(input('Digite um número: '))
    while True:
        print('Você escolhe par ou ímpar?\n[0] Par\n[1] Ímpar')
        par = int(input('R: '))
        if par == 0 or par == 1:
            break
        print('Digite uma opção válida!')
    num2 = (num + comp) % 2
    print(f'Você jogou {num} e o computador jogou {comp}')
    if par == num2:
        counter += 1
        print('Você coseguiu! Vamos novamente')
    else:
        break
print(f'Não foi dessa vez! Você venceu {counter} vezes do compuador')
