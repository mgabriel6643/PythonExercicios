print('Os números pares entre 1 e 50 são: ')
for c in range(1, 51):
    if c % 2 == 0:
        if c == 50:
            print('{}.'.format(c))
        else:
            print('{}'.format(c), end=', ')
