from time import sleep


def maior(* valores):
    cont = m = 0
    print('=' * 50)
    print('Analisando os valores passados...')
    for num in valores:
        print(f'{num}', end=' ')
        sleep(0.5)
        if cont == 0:
            m = num
        else:
            if num > m:
                m = num
        cont += 1
    print(f'Foram informados {cont} valores ao todo.')
    print(f'O maior valor informado foi {m}.')


# Programa Principal
maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
