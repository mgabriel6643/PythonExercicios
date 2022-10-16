n20 = n10 = n1 = r50 = r20 = r10 = 0
print('=' * 30)
print('{:^30}'.format('BANCO CEV'))
print('=' * 30)
saque = int(input('Digite o valor que deseja sacar: R$'))
while True:
    n50 = saque // 50
    r50 = saque % 50
    if r50 == 0:
        break
    n20 = r50 // 20
    r20 = r50 % 20
    if r20 == 0:
        break
    n10 = r20 // 10
    r10 = r20 % 10
    if r10 == 0:
        break
    n1 = r10 // 1
    break
print(f'''{n50} notas de R$50,00
{n20} notas de R$20,00
{n10} notas de R$10,00
{n1} notas de R$ 1,00''')
