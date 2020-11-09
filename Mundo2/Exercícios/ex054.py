from datetime import date

# lis = []
counter = 0
today = date.today().year

for i in range(0, 7):
    year = int(input('Digite seu ano de nascimento: '))
    if (today - year) > 18:
        # lis.append(year)
        counter += 1
if counter == 1:
    print('Foi encontrada {} pessoa maior de idade e {} menores'.format(counter, (7 - counter)))
else:
    print('Foram encontradas {} pessoas maiores de idade e {} menores'.format(counter, (7 - counter)))
