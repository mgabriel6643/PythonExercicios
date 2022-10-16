print('{:=^40}'.format(' LOJAS GUANABARA '))
valor = float(input('Qual o valor do produto? R$'))
print('''FORMAS DE PAGAMENTO
1 - À vista dinheiro/cheque
2 - À vista no cartão
3 - Em até 2x no cartão
4 - 3x ou mais no cartão''')
pag = int(input(''))
if pag == 1:
    tot = valor * 0.9
elif pag == 2:
    tot = valor * 0.95
elif pag == 3:
    tot = valor
    parc = tot / 2
    print('Sua compra será parcelada em 2x de R${:.2f} SEM JUROS'.format(parc))
elif pag == 4:
    tot = valor * 1.20
    totparc = int(input('Sua compra será parcelada em quantas vezes? '))
    parcela = tot/totparc
    print('Sua compra será parcelada em {}x de R${:.2f} COM JUROS'.format(totparc, parcela))
else:
    tot = valor
    print('OPÇÃO INVÁLIDA de pagamento. Tente novamente.')
print('O produto sairia por R${:.2f}, pela sua escolha de método de pagamento, sairá por R${:.2f}'.format(valor, tot))
