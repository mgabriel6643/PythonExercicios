contador = 1
n1 = float(input('Digite o primeiro valor: '))
s = maior = menor = n1
continua = str(input('Deseja continuar a digitar?[S/N] ')).upper().strip()[0]
while continua != 'N':
    n1 = float(input('Digite o próximo valor: '))
    contador += 1
    s += n1
    if n1 > maior:
        maior = n1
    if n1 < menor:
        menor = n1
    continua = str(input('Deseja continuar a digitar? [S/N]: ')).upper().strip()[0]
media = s / contador
print('Você digitou {} números, sua soma é {}, média entre eles é {}, o menor é {} e o maior {}'.format(contador, s, media, menor, maior))
