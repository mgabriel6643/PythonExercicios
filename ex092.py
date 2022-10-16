from datetime import datetime
dados = dict()
dados['Nome'] = str(input('Nome: ')).strip().title()
dados['Idade'] = datetime.today().year - int(input('Ano de Nascimento: '))
dados['CTPS'] = int(input('Carteira de Trabalho (0 não tem): '))
if dados['CTPS'] != 0:
    dados['Contratação'] = int(input('Ano de contratação: '))
    dados['Salário'] = float(input('Salário: R$'))
    dados['Aposentadoria'] = dados['Idade'] + 35 - (datetime.today().year - dados['Contratação'])
print('=' * 30)
for k, v in dados.items():
    print(f'{k} é igual a {v}')
