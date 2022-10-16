from random import randint
from time import sleep
n1 = randint(0, 5)  # Faz o computador 'PENSAR' em um número
print('-=-' * 20)
print('Vou pensar em um número de 0 a 5. Tente adivinhar...')  # Jogador tenta adivinhar
print('-=-' * 20)
n2 = int(input('Em que número pensei? '))
print('PROCESSANDO...')
sleep(3)
if n2 == n1:
    print('Parabéns, você acertou!')
else:
    print('Eu venci!Pensei no número {} e não no {}. Muahaha!'.format(n1, n2))
