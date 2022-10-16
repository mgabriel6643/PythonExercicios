from time import sleep
f = 1
print('=' * 20)
print('CÁLCULO DE FATORIAL')
print('=' * 20)
c = int(input('Digite um número para saber seu fatorial: '))
sleep(1)
print('{}! = '.format(c), end='')
while c > 0:
    if c != 1:
        print('{}'.format(c), end=' x ')
    else:
        print(c, end=' = ')
    f = f * c
    c = c - 1
print(f)
