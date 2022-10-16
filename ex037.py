n1 = int(input('Digite o número que deseja converter: '))
print('''Escolha para que base deseja converter: 
1 - BINÁRIO
2 - OCTAL
3 - HEXADECIMAL''')
n2 = int(input('SUA OPÇÃO:'))
if n2 == 1:
    n3 = bin(n1)
    n2 = 'binário'
elif n2 == 2:
    n3 = oct(n1)
    n2 = 'octal'
else:
    n3 = hex(n1)
    n2 = 'hexadecimal'
if n2 == 1 or n2 == 2 or n2 == 3:
    print('O número {} em {} é {}'.format(n1, n2, n3[2:]))
else:
    print('Digite uma opção VÁLIDA')
