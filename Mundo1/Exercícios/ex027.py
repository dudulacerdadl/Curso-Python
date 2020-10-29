name = input('Digite o seu nome completo: ').strip()
completeName = name.split()

print('Seu primeiro nome: {}\nSeu último nome: {}'.format(completeName[0], completeName[len(completeName)-1]))
