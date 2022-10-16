from random import randint
c = 0
n2 = 1
print('Sou seu computador...')
n1 = randint(0, 10)  # faz o computador pensar em um número
print('Acabei de pensar em um número de 0 a 10.')
print('Será que você consegue adivinhar qual foi?')
while n2 != n1:
    n2 = int(input('Qual o seu palpite? '))  # Lê palpite do jogador
    c += 1
    if n2 < n1:
        print('Mais...Tente mais uma vez.')
    if n2 > n1:
        print('Menos...Tente mais uma vez.')
if c == 1:
    print('Depois de {} tentativa você acertou, parabéns pelo cagaço'.format(c))
if c <= 3:
    print('Depois de {} tentativas você acertou, parabéns pelo mínimo'.format(c))
if c > 3:
    print('Depois de {} tentativas você acertou, chutando assim até eu'.format(c))
