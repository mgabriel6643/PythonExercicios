nome = input('Digite o nome do funcionário: ')
n1 = float(input('Digite o salário de {}: R$'.format(nome)))
print('O novo salário de {} com aumento de 15% será de R${:.2f}'.format(nome, n1 * 1.15))
