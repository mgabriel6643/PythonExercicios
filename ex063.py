a = 0
b = 1
contador = 3
print('=' * 22)
print('SEQUÊNCIA DE FIBONACCI')
print('=' * 22)
n1 = int(input('Digite a quantidade de termos da sequência de fibonacci deseja ver: '))
print('~' * 22)
print('{} → {}'.format(a, b), end=' → ')
while contador <= n1:
    c = a + b
    a = b
    b = c
    print(c, end=' → ')
    contador += 1
print('FIM')
print('~' * 22)
