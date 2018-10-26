print('Gerador de PA')
print('--'*10 )
p_termo=int(input('Primeiro Termo: '))
r= int(input('RAZÃO: '))
termo=p_termo
cont = 1
total = 0
mais = 10
while mais != 0:
    total=total + mais
    while cont<=total:
        print('{} ->'.format(termo), end='')
        termo+=r
        cont+=1
    print('PAUSA')
    mais=int(input('Quantos Termos você quer mostrar a mais: '))
print('Progressão finalizada com {} termos mostrados'.format(total))
