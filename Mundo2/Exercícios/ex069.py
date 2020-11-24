counterYars = 0
counterMale = 0
counterFame = 0

while True:
    age = int(input('Digite sua idade: '))
    sex = input('Digite o seu sexo [M/F]: ').upper()
    while sex != 'M' and sex != 'F':
        sex = input('Digite uma opção válida! [M/F]: ').upper()
    if age > 18:
        counterYars += 1
    if sex == 'M':
        counterMale += 1
    if sex == 'F' and age < 20:
        counterFame += 1
    option = input('Deseja continuar [S/N]: ').upper()
    while option != 'S' and option != 'N':
        option = input('Digite uma opção válida! [S/N]: ').upper()
    if option == 'N':
        break
print(f'Foram consultadas:\n'
      f'{counterYars} pessoas maiores de idade.\n'
      f'{counterMale} pessoas do sexo masculino. \n'
      f'{counterFame} pessoas do sexo feminino menores de 20 anos.')
