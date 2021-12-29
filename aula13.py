salario = float(input('Qual seu salario? R$'))
almento = salario + (salario * 15 / 100)
print('Um funcionario que ganhava R${:.2f}, com 15% de aumento, passara a ganhar R${:.2f}'.format(salario, almento))
