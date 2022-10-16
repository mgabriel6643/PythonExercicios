dados = dict()
golspart = list()
totgols = 0
dados['Nome'] = str(input('Nome do jogador: ')).strip().title()
dados['Partidas'] = int(input('Total de partidas: '))
for c in range(0, dados['Partidas']):
    golspart.append(int(input(f'Número de gols da partida {c + 1}: ')))
    totgols += golspart[c]
dados['Gols por partida'] = golspart
dados['Total de gols'] = totgols
print('=' * 80)
print(dados)
for k, v in dados.items():
    print(f'O campo {k} tem o valor {v}')
print('=' * 80)
print(f'O jogador {dados["Nome"]} jogou {dados["Partidas"]} partidas.')
for i in range(0, dados["Partidas"]):
    print(f'    →Na partida {i + 1}, fez {dados["Gols por partida"][i]} gols.')
