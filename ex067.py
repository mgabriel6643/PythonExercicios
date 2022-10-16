titulo = 'TABUADA'
print('=' * 20)
print(f'{titulo:^20}')
print('=' * 20)
while True:
    n1 = int(input('Digite o número do qual deseja saber a tabuada (para parar digite um número negativo): '))
    if n1 < 0:
        break
    for c in range(1, 11):
        print(f'{n1} x {c:>2} = {n1 * c:02d}')
    print('-' * 20)
print('-' * 20)
print('FIM DO PROGRAMA')
