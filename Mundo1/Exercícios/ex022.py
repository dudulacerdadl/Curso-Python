name = input('Digite o seu nome completo: ').strip()

print('Nome maiúsculo: {}'.format(name.upper()))
print('Nome minúsculo: {}'.format(name.lower()))

nameList = name.split()
newName = ''.join(nameList)

# print('Tamanho do nome sem espaços: {}'.format(len(name) - name.count(' ')))
# print('Tamanho do primeiro nome: {}'.format(name.find(' ')))
print('Tamanho do nome sem espaços: {}'.format(len(newName)))
print('Tamanho do primeiro nome é {} e tem {} letras'.format(nameList[0], len(nameList[0])))
