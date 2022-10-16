n1 = int(input('Quantos dias alugados? '))  # dias alugados
n2 = float(input('Quantos km rodados? '))  # km rodados
print('O total a pagar é de R${:.2f}'.format((60 * n1) + (0.15 * n2)))
