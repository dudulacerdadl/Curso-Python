phrase = str(input('Digite uma frase: '))
uPhrase = phrase.replace(' ', '').lower()
u2 = ''

for i in range(len(uPhrase)-1, -1, -1):
    u2 += uPhrase[i]
print('O inverso de {} é {}'.format(uPhrase, u2))
if u2 == uPhrase:
    print('A frase é um palíndromo')
else:
    print('A frase não é um palíndromo')
