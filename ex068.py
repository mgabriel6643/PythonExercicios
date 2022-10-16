from random import randint
c = 0
while True:
    while True:  # Garante que o jogador escolhar PAR ou IMPAR
        d = str(input('Escolha IMPAR ou PAR: ')).upper().strip()  # Jogador escolhe PAR OU IMPAR
        if d == 'PAR' or d == 'IMPAR':
            break
        else:
            print('Digite uma opção válida')
    while True:  # Garante que o jogador escolha um número entre 0 e 5
        n1 = int(input('Escolha um número natural entre 0 e 5: '))  # Jogador escolhe o número a apostar
        if 0 <= n1 <= 5:
            break
        else:
            print('Digite um número válido')
    n2 = randint(0, 5)  # PC escolhe o número a apostar
    soma = n1 + n2
    print(f'O PC escolheu {n2} e o jogador {n1}')
    c += 1
    if soma % 2 == 0 and d == 'IMPAR' or soma % 2 != 0 and d == 'PAR':
        break
print(f'Você perdeu após {c} tentativas')
