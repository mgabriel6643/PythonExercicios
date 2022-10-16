n1 = int(input('Digite o primeiro número inteiro: '))
n2 = int(input('Digite o segundo número inteiro: '))
if n1 > n2:
    print('O {}PRIMEIRO{} valor é maior'.format('\033[1;34m', '\033[m'))
elif n1 < n2:
    print('O {}SEGUNDO{} valor é maior'.format('\033[1;34m', '\033[m'))
else:
    print('Ambos números digitados são {}IGUAIS{}'.format('\033[1;34m', '\033[m'))
