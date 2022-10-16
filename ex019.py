from random import choice
n1 = input('Insira o nome do primeiro aluno: ')
n2 = input('Insira o nome do segundo: ')
n3 = input('Insira o nome do terceiro: ')
n4 = input('Insira o nome do quarto: ')
print('O aluno escolhido é {}'.format(choice([n1, n2, n3, n4])))
