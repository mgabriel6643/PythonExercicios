import random
from time import sleep
computador = random.choice(['PEDRA', 'PAPEL', 'TESOURA'])
print('=' * 20)
print('JOKENPÔ')
print('=' * 20)
jogador = int(input('''Escolha:
[ 1 ] - PEDRA
[ 2 ] - PAPEL
[ 3 ]- TESOURA
'''))
print('JO')
sleep(1)
print('KEN')
sleep(2)
print('PO!!!')
print('=' * 51)
if jogador == 1:
    jogador = 'PEDRA'
elif jogador == 2:
    jogador = 'PAPEL'
else:
    jogador = 'TESOURA'
print('Você escolheu {} e o computador escolheu {}'.format(jogador, computador))
if computador == jogador:
    print('EMPATE')
elif computador == 'PEDRA' and jogador == 'TESOURA' or computador == 'PAPEL' and jogador == 'PEDRA' or computador == 'TESOURA' and jogador == 'PAPEL':
    print('Você {}PERDEU{}'.format('\033[1;31m', '\033[m'))
else:
    print('Você {}VENCEU!!!!{}'.format('\033[1;32m', '\033[m'))
