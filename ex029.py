v1 = int(input('Em que velocidade(km/h) estava o carro? '))
if v1 > 80:
    print('Você estava a {}km/h e a velocidade máxima na via é de 80km/h'.format(v1))
    print('Você foi MULTADO em R${:.2f}'.format(7 * (v1 - 80)))
else:
    print('Tenha um bom dia! Dirija com segurança!')
