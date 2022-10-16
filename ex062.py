n1 = int(input('Digite o primeiro termo da PA: '))
n2 = int(input('Digite a razão da PA: '))
c = 0
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while c < total:
        print('{}'.format(n1), end=' → ')
        n1 = n1 + n2
        c += 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais? '))
print('Progressão finalizada com {} termos mostrados.'.format(total))