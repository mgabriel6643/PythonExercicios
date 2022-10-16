sexo = ' '
while sexo != 'M' and sexo != 'F':
    sexo = str(input('Digite o sexo da pessoa [M/F]: ')).strip().upper()
    if sexo != 'M' and sexo != 'F':
        print('DIGITE UMA OPÇÃO VÁLIDA')
print('O sexo digitado foi {}'.format(sexo))
