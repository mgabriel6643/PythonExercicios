from random import randint
from time import sleep
escolha = list()
temporario = list()
print('=' * 30)
print(f'{"JOGA NA MEGA SENA":^30}')
print('=' * 30)
jogos = int(input('Quantos jogos serão realizados? '))
for i in range(0, jogos):
    count = 0
    while count < 6:
        temp = randint(0, 60)
        if temp not in escolha:
            temporario.append(temp)
            temporario.sort()
            count += 1
    escolha.append(temporario[:])
    temporario.clear()
print('=' * 5,f'SORTEANDO {jogos:02d} JOGOS', '=' * 5)
print('Os números escolhidos para as apostas foram: ')
for c in range(0, len(escolha)):
    sleep(1)
    print(f'Jogo {c + 1}: {escolha[c]}')
