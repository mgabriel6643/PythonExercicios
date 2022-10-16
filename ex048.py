s = 0
n = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        s += c
        n += 1
        if c == 495:
            print('{}'.format(c))
        else:
            print('{}'.format(c), end=', ')
print('O total de números divisíveis por 3 que são ímpares entre 0 e 500 é {}'.format(n), end=' ')
print('e sua soma é {}'.format(s))
