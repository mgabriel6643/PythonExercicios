matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
soma = soma3c = maior2l = somapar = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite o elemento N{l + 1},{c + 1}: '))
        soma += matriz[l][c]
        soma3c += matriz[l][2]
        if matriz[l][c] % 2 == 0:
            somapar += matriz[l][c]
        if c == 0:
            maior2l = matriz[1][c]
        elif matriz[1][c] > maior2l:
            maior2l = matriz[1][c]
print('=' * 30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()
print('=' * 30)
print(f'A soma de todos os valores da matriz foi {soma}', end=', ')
print(f'de todos os pares {somapar}', end=', ')
print(f'dos valores da terceira coluna foi {soma3c}', end=' e ')
print(f'o maior valor da linha 2 foi {maior2l}.')
