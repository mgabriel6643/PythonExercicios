cont = soma = 0
while True:
    numero = int(input('Digite um número inteiro (se deseja terminar, digite 999): '))
    if numero == 999:
        break
    cont += 1
    soma += numero
print(f'Foram digitados {cont} números e a soma entre eles é {soma}')
