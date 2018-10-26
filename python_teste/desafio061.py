print('Gerador de PA')
print('--'*10 )
p_termo=int(input('Primeiro Termo: '))
r= int(input('RAZÃO: '))

termo=p_termo
cont = 1

while cont <= 10:
    print('{} ->'.format(termo), end='')
    termo+=r
    cont+=1
print('Acabou')
