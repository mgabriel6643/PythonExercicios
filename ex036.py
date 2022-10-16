valor = float(input('Digite o valor da casa que deseja financiar: R$'))
salario = float(input('Digite o valor do seu salário atual: R$'))
ano = int(input('Em quantos anos deseja pagar? '))
meses = ano * 12
prestacao = valor/meses
if prestacao <= 0.3 * salario:
    print('Seu empréstimo foi {}APROVADO{} você pagará {} prestações no valor de R${:.2f}'.format('\033[1;32m', '\033[m',meses, prestacao))
else:
    print('Seu empréstimo foi {}NEGADO{}, o valor da casa e quantidade de prestações, são incompatíveis com seu salário.'.format('\033[1;31m', '\033[m'))
