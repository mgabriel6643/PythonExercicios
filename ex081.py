valores = list()
c = 1
while True:
    valores.append(int(input(f'Digite o {c}° valor: ')))
    continua = ' '
    while continua not in 'NS':  # Repetição caso usuário digite != N or S
        continua = str(input('Deseja continuar?[S/N]: ')).strip().upper()[0]
    if continua == 'N':
        break
    c += 1
print('=' * 30)
print(f'Foram digitados {c} valores nesta ordem: {valores}')
valores.sort(reverse=True)  # organiza valores em ordem decrescente
print(f'Valores em ordem descrescente: {valores}')
if 5 in valores:
    print('O valor 5 faz parte da lista!')
else:
    print('O valor 5 não faz parte da lista.')
