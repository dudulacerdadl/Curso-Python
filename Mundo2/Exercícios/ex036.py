value = float(input('Digite o valor da casa: '))
salary = float(input('Digite o seu salário: '))
years = int(input('Digite em quantos anos deseja pagar: '))
installment = value / (years * 12)

print('O valor da sua casa será de R${:.2f} pago em {} anos, com mensalidade de R${:.2f}'.format(value, years, installment))

if installment > (salary * (30/100)):
    print('Infelizmene, seu empréstimo foi NEGADO')
else:
    print('Parabéns! Seu emprestimo foi APROVADO')
