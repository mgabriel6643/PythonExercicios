print('-=' * 20)
print('ANALISADOR DE TRIÂNGULOS')
print('-=' * 20)
n1 = float(input('Digite o comprimento do primeiro segmento de reta: '))
n2 = float(input('Digite o comprimento do segundo segmento de reta: '))
n3 = float(input('Digite o comprimento do terceiro segmento de reta: '))
if n1 >= n2 + n3:
    print('Os segmentos de reta de comprimento {}, {} e {}, NÃO podem formar um triângulo'.format(n1, n2, n3))
else:
    if n2 >= n1 + n3:
        print('Os segmentos de reta de comprimento {}, {} e {}, NÃO podem formar um triângulo'.format(n1, n2, n3))
    else:
        if n3 >= n1 + n2:
            print('Os segmentos de reta de comprimentos {}, {} e {}, NÃO podem formar um triângulo'.format(n1, n2, n3))
        else:
            print('Os segmentos de reta de comprimentos {}, {} e {}, podem formar um triângulo'.format(n1, n2, n3))
