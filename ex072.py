cont = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze',
        'Doze', 'Treze', 'Quatorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')
while True:
    print('=' * 60)
    while True:
        n = int(input('Digite o número entre 0 e 20 para visualizá-lo por extenso: '))
        if n < 0 or n > 20:
            print('ERRO! Número digitado não se encontra entre 0 e 20')
        else:
            break
    print(f'{n} → {cont[n]}')
    continua = ' '
    while continua not in 'NS':
        continua = str(input('Deseja continuar?[S/N] ')).upper().strip()[0]
    if continua == 'N':
        break
print('PROGRAMA FINALIZADO')
