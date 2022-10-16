n1 = float(input('Digite uma medida em metros: '))
print('{}km \n{}hm \n{}dam \n{}m \n{:.0f}dm \n{:.0f}cm \n{:.0f}mm'.format(n1/1000, n1/100, n1/10, n1, n1*10, n1*100, n1*1000))
