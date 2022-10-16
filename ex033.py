n1 = float(input('Digite o 1° número: '))
n2 = float(input('Digite o 2° número: '))
n3 = float(input('Digite o 3° número: '))
if n1 < n2:
    a = n2
    b = n1
else:
    a = n1
    b = n2
if a < n3:
    a = n3
else:
    a = a
if b > n3:
    b = n3
else:
    b = b
print('Dentre os números digitados {}, {} e {}, o maior é {} e o menor é {}'.format(n1, n2, n3, a, b))
