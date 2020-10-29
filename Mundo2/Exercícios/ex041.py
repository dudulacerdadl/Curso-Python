from datetime import date

years = int(input('Digite o seu ano de nascimento: '))
old = date.today().year - years

print('O atleta tem {} anos'.format(old))

if old <= 9:
    print('MIRIM')
elif old <= 14:
    print('INFANTIL')
elif old <= 19:
    print('JUNIOR')
elif old <= 25:
    print('SÊNIOR')
else:
    print('MASTER')
