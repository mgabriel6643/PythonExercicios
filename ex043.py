peso = float(input('Qual é o seu peso em kg? '))
altura = float(input('Qual a sua altura em m? '))
imc = peso / (altura ** 2)
if imc < 18.5:
    clas = 'ABAIXO DO PESO'
    cor = '\033[1;31m'
elif imc < 25:
    clas = 'com PESO IDEAL'
    cor = '\033[1;32m'
elif imc < 30:
    clas = 'com SOBREPESO'
    cor = '\033[1;33m'
elif imc < 40:
    clas = 'com OBESIDADE'
    cor = '\033[1;31m'
else:
    clas = 'com OBESIDADE MÓRBIDA'
    cor = '\033[7;31m'
print('Você está classificado {}{}{}'.format(cor, clas, '\033[m'))
