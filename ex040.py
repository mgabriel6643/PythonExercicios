n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
media = (n1 + n2)/2
if media <= 5:
    sit = 'REPROVADO'
    cor = '\033[1;31m'
elif 5 < media < 7:
    sit = 'RECUPERAÇÃO'
    cor = '\033[1;33m'
else:
    sit = 'APROVADO'
    cor = '\033[1;32m'
print('Tirando {} e {} a média do aluno é {:.2f} e ele está {}{}{}'.format(n1, n2, media, cor, sit, '\033[m'))
