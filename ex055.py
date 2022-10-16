maiorp = 0
menorp = 0
for c in range(1, 6):
    peso = int(input('Digite o {}° peso em kg: '.format(c)))
    if c == 1:
        maiorp = peso
        menorp = peso
    else:
        if peso > maiorp:
            maiorp = peso
        if peso < menorp:
            menorp = peso
print('O menor peso digitado foi {}kg e o menor {}kg'.format(menorp, maiorp))
