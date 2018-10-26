
num=int(input('Digite um numero para Calcular seu Fatorial: ' ))
calc=num
fat=1
print('Calculando {}!= '.format(calc), end='')
while calc > 0:
   print('{}'.format(calc), end='')
   print('x' if calc>1 else '=', end='')
   fat*=calc
   calc-=1
print('{}'.format(fat))

