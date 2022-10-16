from random import randint
maior = menor = 0
aleatorio = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))
print('Os valores sorteados foram: ',end='')
for count in range(0, 5):
    print(f'{count} ', end='')
print(f'\nO maior número gerado foi {max(aleatorio)} e o menor {min(aleatorio)}.')
