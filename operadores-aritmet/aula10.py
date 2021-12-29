carteira = float(input('Digite quanto tem na sua carteira? R$'))
dollar = carteira / 5.64
print('Com R${:.2f} você pode comprar US${:.2f}'.format(carteira, dollar))

