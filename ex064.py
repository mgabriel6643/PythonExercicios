cont = s = 0
c = float(input('Se deseja parar, digite 999, caso não, digite um número: '))
while c != 999:
    cont += 1
    s += c
    c = float(input('Se deseja parar, digite 999, caso não, digite um número: '))
print('Você digitou {} números e sua soma é {}'.format(cont, s))
print('FIM')
