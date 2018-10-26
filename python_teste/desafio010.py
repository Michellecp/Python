din=float(input('Quanto de dinheiro você tem na carteira? R$'))
dolar = din/3.25
euro = din/3.86
print('Com {:.2f} da para comprar US$ {:.2f}'.format(din, dolar))
print('Com {:.2f} da para comprar {:.2f} euros'.format(din, euro))