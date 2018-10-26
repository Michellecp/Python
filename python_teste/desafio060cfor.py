from math import factorial

num=int(input('Digite um numero para Calcular seu Fatorial: ' ))
calc=num
fat=1
resul=0
print('Calculando {}!= '.format(calc), end='')

for calc in range(num, fat, -1):
    print('{}'.format(calc), end='')
    print('x' if calc > 1 else '=', end='')

    fatorial(calc)

print('{}'.format(fat))
