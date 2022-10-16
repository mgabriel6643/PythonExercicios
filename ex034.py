n1 = float(input('Qual o valor do salário do funcionário? R$'))
if n1 > 1250.00:
    n2 = 1.1 * n1
else:
    n2 = 1.15 * n1
print('Quem ganhava R${:.2f} passa a ganhar R${:.2f}'.format(n1, n2))
