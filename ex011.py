n1 = float(input('Qual a altura da parede em metros? '))  # Altura
n2 = float(input('Qual a largura da parede também em metro? '))  # Largura
a = n1 * n2  # Área
t = a / 2  # Volume de tinta

print('A área de uma parede com as dimensões {}m x {}m é de {:.2f}m²'.format(n1, n2, a))
print('Para pintá-la serão necessários {:.2f}l de tinta'.format(t))

