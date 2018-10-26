num1=int(input('Primeiro Numero:'))
num2=int(input('Segundo Numero:'))
num3=int(input('Terceiro Numero:'))

menor=num1
if num2<num1 and num2<num3 :
    menor=num2
if num3<num1 and num3<num2:
    menor=num3

maior=num1
if num2>num1 and num2>num3 :
    maior=num2
if num3>num1 and num3>num2 :
    maior=num3

print('Menor numero é {}'.format(menor))
print('Maior numero é {}'.format(maior))
