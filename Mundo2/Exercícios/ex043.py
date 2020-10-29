weigth = float(input('Digite o seu peso: '))
height = float(input('Digite a sua altura em metros: '))
imc = weigth / (height ** 2)

print('Seu IMC é {:.1f}'.format(imc))

if imc < 18.5:
    print('Abaixo do Peso')
elif imc < 25:
    print('Peso ideal')
elif imc < 30:
    print('Sobrepeso')
elif imc < 40:
    print('Obesidade')
else:
    print('Obesiadade mórbida')
