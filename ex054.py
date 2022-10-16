from datetime import date
m21 = 0
for c in range(1, 8):
    nasc = int(input('Digite o ano de nascimento da {}° pessoa: '.format(c)))
    idade = date.today().year - nasc
    if idade >= 21:
        m21 = m21 + 1
print('Das pessoas identificadas, {} são maiores de idade e {} são menores de idade'.format(m21, 7 - m21))