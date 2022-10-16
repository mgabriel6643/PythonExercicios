n1 = int(input('Digite um número natural: '))
d = 0
fcor = '\033[m'
for c in range(1, n1 + 1):
    if n1 % c == 0:
        d = d + 1
if d == 2:
    print('O número {} tem {} divisores, logo é {}PRIMO{}'.format(n1, d, '\033[1;34m', fcor))
else:
    print('O número {} tem {} divisores, logo {}NÃO É PRIMO{}'.format(n1, d, '\033[1;31m', fcor))
