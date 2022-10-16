completa = list()
par = list()
impar = list()
c = 1
while True:
    completa.append(int(input(f'Digite o {c}° número: ')))
    continua = ' '
    while continua not in 'NS':
        continua = str(input('Deseja continuar?[S/N] ')).strip().upper()[0]
    if continua == 'N':
        break
    c += 1
for i, v in enumerate(completa):
    if v % 2 == 0:
        par.append(completa[i])
    else:
        impar.append(completa[i])
print(f'Os números digitados foram: {completa}', end=', ')
print(f'destes os pares são {par}', end=' ')
print(f'e os ímpares são {impar}')
