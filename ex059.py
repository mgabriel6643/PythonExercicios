from time import sleep
n1 = float(input('Digite um valor: '))
n2 = float(input('Digite outro valor: '))
n3 = 0
print('=' * 30)
while n3 != 5:
    print('''[ 1 ] SOMAR
[ 2 ] MULTIPLICAR
[ 3 ] MAIOR
[ 4 ] NOVOS NÚMEROS
[ 5 ] SAIR DO PROGRAMA''')
    n3 = int(input('Escolha uma das alternativas: '))
    if n3 == 1:
        print('{} + {} = {}'.format(n1, n2, n1 + n2))
    if n3 == 2:
        print('{} x {} = {}'.format(n1, n2, n1 * n2))
    if n3 == 3:
        if n1 == n2:
            print('Os números digitados são iguais e tem o valor de {}'.format(n1))
        if n1 > n2:
            maior = n1
            menor = n2
            print('{} > {}'.format(maior, menor))
        if n1 < n2:
            maior = n2
            menor = n1
            print('{} > {}'.format(maior, menor))
    if n3 == 4:
        n1 = float(input('Digite um valor: '))
        n2 = float(input('Digite outro valor: '))
    if n3 > 5:
        print('CÓDIGO INCORRETO, redigite o código de acordo com o menu')
    sleep(1)
    print('=' * 30)
print('Fim do programa, volte sempre!')