d1 = float(input('Digite a distância a ser percorrida durante a viagem em km: '))
print('Você está prestes a começar uma viagem de {:.1f}km'.format(d1))
if d1 <= 200:
    passagem = 0.5 * d1
else:
    passagem = 0.45 * d1
print('E o valor da sua passagem será de R${:.2f}'.format(passagem))
