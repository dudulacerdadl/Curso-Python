sum = 0
counter = 0
oldder = 0
oldderName = ''

for i in range(0, 4):
    name = input('Digite um nome: ').strip()
    old = int(input('Digite uma idade: '))
    print('Qual o seu sexo:\n[1] Feminino\n[2] Masculino')
    sex = int(input('R: '))

    sum += old
    # if i == 1 and sex == 2:
    #     oldder = old
    #     oldderName = name
    if sex == 2 and old > oldder:
        oldder = old
        oldderName = name
    if sex == 1 and old < 21:
        counter += 1

media = sum / 4
print('A média de idade indicada é de {} anos'.format(media))
print('O homem mais velho tem {} anos e se chama {}'.format(oldder, oldderName))
print('O número de mulheres menores de 21 anos é de {}'.format(counter))