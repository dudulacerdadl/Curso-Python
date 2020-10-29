num = int(input('Digite um número entre 0 e 9999: '))
uni = num // 1 % 10
des = num // 10 % 10
cen = num // 100 % 10
mil = num // 1000 % 10

print("""O número digitado foi {}.

Unidades: {}.
Dezenas: {}.
Centenas: {}.
Milhar: {}.""".format(num, uni, des, cen, mil))

# ???
