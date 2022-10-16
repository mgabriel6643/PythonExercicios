dados = list()
temp = list()
i = j = 0
for i in range(1, 4):
    for j in range(1, 4):
        temp.append(int(input(f'Digite o número N{i},{j}: ')))
    dados.append(temp[:])
    temp.clear()
print('=' * 30)
for i in range(0, 3):
    for j in range(0, 3):
        print(f'[{dados[i][j]:^5}]', end=' ')
    print()
