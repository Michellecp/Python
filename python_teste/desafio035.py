print('-*-'*15, '\nAnalisador de Triângulo')
print('-*-'*15 )
a=float(input('Primeiro Segmento: '))
b=float(input('Segundo Segmento: '))
c=float(input('Terceiro Segmento '))

if a+b>c and b+c>a and a+c>b :
    print('Os Segmento acima PODEM formar um triangulo')
else:
    print('Os Segmentos acima NÃO PODEM formar um Triangulo')