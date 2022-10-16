print('=' * 20)
print('TESTE DE PALÍNDROMO')
print('=' * 20)
frase = str(input('Digite o possível palíndromo (sem acentos): ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = junto[::-1]
print('O inverso de {} é {}'.format(frase, inverso))
if inverso == junto:
    print('Temos um palíndromo!')
else:
    print('A frase digitada não é um palíndromo!')
