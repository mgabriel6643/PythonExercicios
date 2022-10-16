dado = list()
lista = list()
maior = menor = 0
while True:
    dado.append(str(input('Nome: ')).strip().title())
    dado.append(float(input('Peso(kg): ')))
    if len(lista) == 0:
        maior = menor = dado[1]
    else:
        if dado[1] > maior:
            maior = dado[1]
        if dado[1] < menor:
            menor = dado[1]
    lista.append(dado[:])
    dado.clear()
    continua = ' '
    while continua not in 'NS':
        continua = str(input('Deseja continuar?[S/N] ')).strip().upper()[0]
    if continua == 'N':
        break
print('=' * 30)
print(lista)
print(f'Foram cadastradas {len(lista)} pessoas')
print(f'O maior peso foi {maior}kg. Peso de ', end='')
for p in lista:
    if p[1] == maior:
        print(f'[{p[0]}]', end=' ')
print()
print(f'O menor peso foi {menor}kg. Peso de ', end='')
for p in lista:
    if p[1] == menor:
        print(f'[{p[0]}]', end=' ')
