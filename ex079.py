valores = list()
c = 1
while True:
    while True:
        valor = int(input(f'Digite o {c}° valor: '))
        if valor in valores:
            print('O valor foi repetido. Não será adicionado.')
        else:
            valores.append(valor)
            print('Valor adicionado com sucesso')
            break
    continua = ' '
    while continua not in 'SN':
        continua = str(input('Deseja continuar?[S/N] ')).strip().upper()[0]
    if continua == 'N':
        break
    c += 1
valores.sort()
print(valores)
