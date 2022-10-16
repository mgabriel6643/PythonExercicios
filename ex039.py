from datetime import date
sexo = str(input('Digite M para sexo masculino e F para sexo feminino: ')).upper()
if sexo == 'F':
    print('Você não tem obrigatoriedade de se alistar')
elif sexo == 'M':
    nascimento = int(input('Digite seu ano de nascimento: '))
    idade = date.today().year - nascimento
    tempo = abs(idade - 18)
    print('Quem nasceu em {} tem {} anos em {}'.format(nascimento, idade, date.today().year))
    if idade < 18:
        print('Você irá se alistar em {} anos'.format(tempo))
        ano = date.today().year + tempo
        print('Seu alistamento será em {}'.format(ano))
    elif idade == 18:
        print('Você deve se alistar esse ano')
    else:
        print('Você deveria ter se alistado há {} anos'.format(tempo))
        ano = date.today().year - tempo
        print('Seu alistamento foi em {}'.format(ano))
else:
    print('ERRO - TENTE NOVAMENTE')
    print('Digite M para masculino e F para feminino')
