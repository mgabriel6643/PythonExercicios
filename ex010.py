n1 = float(input('Quanto dinheiro você deseja converter? R$'))
cot = float(input('Qual a atual cotação do Dólar em Real? '))
conv = n1 / cot
print('Segundo a cotação atual de R$/US${}, você pode comprar US${:.2f}'.format(cot, conv))
