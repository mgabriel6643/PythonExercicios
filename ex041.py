from datetime import date
nascimento = int(input('Digite o ano do seu nascimento: '))
idade = date.today().year - nascimento
print('O atleta tem {} anos'.format(idade))
if idade <= 9:
    clas = 'MIRIM'
elif idade <= 14:
    clas = 'INFANTIL'
elif idade <= 19:
    clas = 'JÚNIOR'
elif idade <= 25:
    clas = 'SÊNIOR'
else:
    clas = 'MASTER'
print('Classificação: {}'.format(clas))
