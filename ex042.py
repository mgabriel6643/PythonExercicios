import os
print('-=' * 20)
print('ANALISADOR DE TRIÂNGULOS')
print('-=' * 20)
n1 = float(input('Digite o comprimento do primeiro segmento de reta: '))
n2 = float(input('Digite o comprimento do segundo segmento de reta: '))
n3 = float(input('Digite o comprimento do terceiro segmento de reta: '))
if n1 <= n2 + n3 and n2 <= n1 + n3 and n3 <= n1 + n2:
    print('Os segmentos de reta {}, {} e {} {}PODEM FORMAR{} um triângulo'.format(n1, n2, n3, '\033[1;32m', '\033[m'), end=' ')
    if n1 == n2 == n3:
        tri = 'EQUILÁTERO'
    elif n1 == n2 or n2 == n3 or n1 == n3:
        tri = 'ISÓSCELES'
    else:
        tri = 'ESCALENO'
    print('{}{}{}'.format('\033[1;32m', tri, '\033[m'))
else:
    print('Os segmentos de reta {}, {} e {} {}NÃO PODEM FORMAR{} um triângulo'.format(n1, n2, n3, '\033[1;31m', '\033[m'))
