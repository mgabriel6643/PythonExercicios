dados = dict()
lista = list()
while True:
    dados['nome'] = str(input('Nome: ')).strip().title()
    dados['sexo'] = str(input('Sexo [M/F]: ')).strip().upper()[0]
    dados['idade'] = int(input('Idade: '))
    lista.append(dados.copy())
    del dados['nome']
    del dados['idade']
    del dados['nome']
    continua = ' '
    while continua not in 'NS':
        continua = str(input('Deseja continuar?[S/N] ')).strip().upper()[0]
    if continua == 'N':
        break
print(lista)
