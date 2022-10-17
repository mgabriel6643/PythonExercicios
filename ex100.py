from random import randint
from time import sleep


def somar_par(lst):
    spar = 0
    for num in lst:
        if num % 2 == 0:
            spar += num
    print(f'Somando os valores pares de {lst}, temos: {spar}')


def sorteia(lst):
    c = 0
    while c < 5:
        lst.append(randint(0, 10))
        c += 1
    print('Sorteando 5 valores da lista:', end=' ')
    for num in lst:
        print(num, end=' → ')
        sleep(0.3)
    print('FIM!')


# Programa principal
lista = list()
sorteia(lista)
somar_par(lista)
