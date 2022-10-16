dados = dict()
dados['Nome'] = str(input('Nome: '))
dados['Média'] = float(input(f'Média de {dados["Nome"]}: '))
if dados['Média'] < 5:
    dados['Situação'] = 'REPROVADO'
elif dados['Média'] < 7:
    dados['Situação'] = 'RECUPERAÇÃO'
else:
    dados['Situação'] = 'APROVADO'
print('=' * 30)
for k, v in dados.items():
    print(f'{k} é igual a {v}')
