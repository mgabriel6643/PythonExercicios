numeros = (int(input('Digite um número: ')), int(input('Digite outro número: ')),
           int(input('Digite mais um número: ')), int(input('Digite o último número: ')))
print(f'Os números digitados foram {numeros}')
print(f'Você digitou o número nove {numeros.count(9)} vezes')
if numeros.count(3) == 0:
    print(f'Você digitou o número três nenhuma vez')
else:
    pos3 = numeros.index(3) + 1
    print(f'O primeiro 3 foi digitado na {pos3}ª posição')
print('Os números pares digitados foram: ', end='')
for c in range(0, 4):
    if numeros[c] % 2 == 0:
        print(numeros[c], end=' ')
