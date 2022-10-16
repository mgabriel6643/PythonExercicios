maior = homem = mjovem = 0
while True:
    print('=' * 20)
    print('CADASTRE UMA PESSOA')
    print('=' * 20)
    idade = int(input('Digite a idade da pessoa: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Digite seu sexo:[M/F] ')).upper().strip()[0]
    if idade > 18:
        maior += 1
    if sexo == 'M':
        homem += 1
    if sexo == 'F' and idade < 20:
        mjovem += 1
    continua = ' '
    while continua not in 'SN':
        continua = str(input('Deseja continuar?[S/N] ')).upper().strip()[0]
    if continua == 'N':
        break
print('=' * 20)
print(f'Das pessoas cadastradas, {maior} têm acima de 18 anos', end=', ')
print(f'{homem} são homens', end=' e ')
print(f'{mjovem} são mulheres abaixo de 20 anos')
