from datetime import date

year = int(input('Digite um ano: '))

if year == 0:
    year = date.today().year

if bool(year % 4 == 0 and year % 100 != 0 or year % 400 == 0):
    print('O ano {} é bissexto'.format(year))
else:
    print('o ano {} não é bissexto'.format(year))
