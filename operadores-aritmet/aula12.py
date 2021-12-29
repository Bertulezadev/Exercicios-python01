produto = float(input('Qual preço do produto? R$'))
desconto = produto - (produto * 5 / 100)
print('O seu produto custava {} e com desconto de 5% vai custa R${} reais'.format(produto, desconto))