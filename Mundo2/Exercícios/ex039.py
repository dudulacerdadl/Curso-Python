from datetime import date

today = date.today().year
years = int(input('Digite o seu ano de nascimento: '))
old = today - years

print('Você nasceu em {} e tem {} anos'.format(years, old))

if old == 18:
    print('Está na hora de se alistar')
elif old < 18:
    print('Ainda não está na hora de se alistar. Faltam {} anos para isso, que será em {}'.format(18 - old, today + (18 - old)))
else:
    print('Já passaram {} anos que você deveria ter se alistado, que era em {}'.format(old - 18, today - (old - 18)))
