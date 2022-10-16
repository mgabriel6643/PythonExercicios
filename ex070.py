total = mais1000 = barato = cont = 0
prodbarato = ''
print('=' * 20)
print('{:^20}'.format('LOJA SUPER BARATÃO'))
print('=' * 20)
while True:
    produto = str(input('Insira o produto que deseja comprar: ')).strip().capitalize().split()
    produto = ' '.join(produto)
    preco = float(input(f'Insira o valor do produto {produto} R$'))
    cont += 1
    total += preco
    if preco > 1000:
        mais1000 += 1
    if cont == 1 or barato > preco:
        barato = preco
        prodbarato = produto
    continua = ' '
    while continua not in 'SN':
        continua = str(input('Deseja continuar?[S/N] ')).upper().strip()[0]
    if continua == 'N':
        break
print('{:-^40}'.format('FIM DO PROGRAMA'))
print(f'O total gasto foi R${total:.2f}, sendo que {mais1000} produtos custaram mais de R$1000,00', end=' ')
print(f'e {prodbarato} foi o produto mais barato, custando R${barato:.2f}')
