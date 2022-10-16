def area(larg, comp):
    return larg * comp


# Programa principal
print('-.' * 15)
print('  CONTROLE DE TERRENOS  ')
print('-.' * 15)
l = float(input('Largura(m): '))
c = float(input('Comprimento(m): '))
a = area(l, c)
print(f'A área de um terreno de {l:.2f}m x {c:.2f}m é de {a:.2f}m².')
