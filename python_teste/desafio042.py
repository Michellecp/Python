print('-*-'*15, '\nAnalisador de Triângulo')
print('-*-'*15 )
a=float(input('Primeiro Segmento: '))
b=float(input('Segundo Segmento: '))
c=float(input('Terceiro Segmento '))

if a+b>c and b+c>a and a+c>b :
    print('Os segmentos acima podem formar um triangulo',end='')
    if a==b==c:
        print(' EQUILÁTERO')
    elif a!=b!=c!=a:
        print(' ISOSCELES')
    else:
        print(' ESCALENO ')
else:
    print('Os Segmentos acima NÃO PODEM formar um Triangulo')


