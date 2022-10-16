n1 = float(input('Digite o preço do produto: R$'))  # preço
n2 = float(input('Qual a porcentagem de desconto? '))
print('O produto que custava R${:.2f} na promoção com desconto de {:.0f}% custará R${:.2f}'.format(n1, n2, n1 * ((100 - n2)/100)))
