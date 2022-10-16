colocacao = ('Palmeiras', 'Internacional', 'Fluminense', 'Corinthians', 'Flamengo', 'Atlhetico-PR', 'Atlético-MG',
             'América-MG', 'Fortaleza', 'Botafogo', 'Santos', 'Goiás', 'São Paulo', 'Bragantino', 'Coritiba',
             'Ceará SC', 'Cuiabá', 'Avaí', 'Atlético-GO', 'Juventude')
print(f'Lista de times: {colocacao}')
print('=' * 290)
print(f'Os cinco primeiros colocados foram: {colocacao[:6]}')
print('=' * 290)
print(f'Os últimos quatro colocados foram: {colocacao[-4:]}')
print('=' * 290)
print(f'Os 20 times em ordem alfabética: {sorted(colocacao)}')
print('=' * 290)
posce = colocacao.index('Ceará SC')
print(f'O Ceará está na {posce + 1}ª posição')
print('=' * 290)
