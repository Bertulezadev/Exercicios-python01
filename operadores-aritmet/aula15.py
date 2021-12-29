dias = int(input ('Quantos dias fico com carro?'))
km = float(input('Quantos KM rodado?'))
pagar = (dias * 60) + (km * 0.15)
print('O total a pagar é R${:.2f}'.format(pagar))
