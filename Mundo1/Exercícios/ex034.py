salary = float(input('Digite o seu salário: '))

if salary > 1250:
    salary += salary * (10/100)
else:
    salary += salary * (15/100)

print('Seu novo salário será de R${:.2f}'.format(salary))
