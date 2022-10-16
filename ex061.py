n1 = int(input('Digite o primeiro termo da PA: '))
n2 = int(input('Digite a razão da PA: '))
c = 0
while c < 10:
    print('{}'.format(n1), end=' → ')
    n1 = n1 + n2
    c += 1
print('FIM')
