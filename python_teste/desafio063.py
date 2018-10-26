print('--'*5)
print('SEQUENCIA FIBONACCI')
print('--'*5)
num=int(input('Quantos termos você quer mostrar? '))
f0=0
f1=1
cont=3
ultimo=num
print('{} -> {}'.format(f0,f1), end='')

while cont <= num:
    f2 = f0 + f1
    print('-> {}'.format(f2), end='')
    cont+=1
    f0=f1
    f1=f2
print('-> FIM')

