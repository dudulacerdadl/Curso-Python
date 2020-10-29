phrase = input('Digite uma frase: ').strip()
a = phrase.lower().count('a')
first = phrase.lower().find('a') + 1
last = phrase.lower().rfind('a') + 1

print('A letra A se repete {} vezes.\nEla aparece pela primeira vez em {}.\nEla para de se repetir em {}'.format(a, first, last))
