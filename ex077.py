objetos = ('smartphone', 'teclado', 'mouse', 'monitor', 'notebook', 'fone', 'carregador', 'mesa')
for c in objetos:
    print(f'\n Na palavra {c.upper()} temos: ', end='')
    for d in c:
        if d.lower() in 'aeiou':
            print(d, end=' ')
