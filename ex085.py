numeros = [[], []]
for c in range(1, 8):
    temp = int(input(f'Digite o {c}° valor: '))
    if temp % 2 == 0:
        numeros[0].append(temp)
    else:
        numeros[1].append(temp)
print('=' * 30)
print(f'Todos os valores digitados: {numeros}')
numeros[0].sort()
numeros[1].sort()
print(f'Valores pares digitados: {numeros[0]}')
print(f'Valores ímpares digitados: {numeros[1]}')
