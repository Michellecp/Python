n1=float(input('Digite sua nota: '))
n2=float(input('Digite sua nota: '))
n=(n1+n2)/2
print('A média foi {:.2f}'.format(n))
if n >=6:
    print('Sua média foi boa. PARABÉNS!!!')
else:
    print('Sua média foi ruim. ESTUDE MAIS!!!')