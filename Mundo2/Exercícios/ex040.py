note1 = float(input('Digite a primeira nota: '))
note2 = float(input('Digite a segunda nota: '))
media = (note1 + note2) / 2

print('Sua média foi {:.1f}'.format(media))
if media < 5:
    print('REPROVADO')
elif media < 7:
    print('RECUPERAÇÃO')
else:
    print('APROVADO')
