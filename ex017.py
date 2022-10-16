from math import hypot
n1 = float(input('Digite o comprimento do primeiro cateto: '))
n2 = float(input('Digite o comprimento do segundo cateto: '))
print('O triângulo formado por catetos de comprimento {:.2f} e {:.2f} tem hipotenusa com valor de {:.2f}'.format(n1, n2, hypot(n1, n2)))
