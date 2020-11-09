sex = input('Digite o sexo desejado [M/F]: ')

while sex not in 'MmFf':
    print('Valor inválido!')
    sex = input('Digite o valor novamente [M/F]: ')
print('FIM')
