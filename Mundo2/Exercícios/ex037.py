num = int(input('Digite um número: '))

print('''\nPara qual base você deseja converter esse número:\n
[1] Binário
[2] Octal
[3] Hexadecimal''')
base = int(input('R:'))

if base == 1:
    print('{} convertido para binário é {}'.format(num, bin(num)[2:]))
elif base == 2:
    print('{} convertido para octal é {}'.format(num, oct(num)[2:]))
elif base == 3:
    print('{} convertido para hexadecimal é {}'.format(num, hex(num)[2:]))
else:
    print('Opção inválida. Tente novamente')
