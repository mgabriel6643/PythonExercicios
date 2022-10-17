from time import sleep


def linha():
    print('=' * 30)


def contador(inicio, fim, passo):
    linha()
    cont = inicio
    passo = abs(passo)
    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}.')
    if passo == 0:
        passo = 1
    if inicio < fim:
        while cont <= fim:
            print(f'{cont}', end=' → ')
            sleep(0.5)
            cont += passo
        print('FIM!')
    else:
        while cont >= fim:
            print(f'{cont}', end=' → ')
            sleep(0.5)
            cont -= passo
        print('FIM!')


# Programa Principal
contador(1, 10, 1)
contador(10, 0, 2)
linha()
print('Agora é sua vez de personalizar a contagem!')
i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
contador(i, f, p)
