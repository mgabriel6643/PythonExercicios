n1 = int(input('Digite o primeiro termo da PA: '))
n2 = int(input('Digite a razão da PA: '))
decimo = n1 + n2 * (10 - 1)
for c in range(n1, decimo + 1, n2):
    if c == decimo:
        print('{}'.format(c))
    else:
        print('{}'.format(c), end=' → ')
