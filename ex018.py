import math
n1 = float(input('Digite o valor do ângulo em graus: '))
n2 = math.radians(n1)
print('sen{:.0f}° = {:.2f}'.format(n1, math.sin(n2)))
print('cos{:.0f}° = {:.2f}'.format(n1, math.cos(n2)))
print('tg{:.0f}° = {:.2f}'.format(n1, math.tan(n2)))
