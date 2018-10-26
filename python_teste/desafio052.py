num=int(input('Digite um numero: '))
tot=0
for c in range(1,num+1):
    if num%c==0:
        print('\33[34m', end='')
        tot+=1
    else:
        print('\33[m', end='')
    print('{} '.format(c), end='')
print('\n\033[mO número {} foi divisivel {} vezes'.format(num, tot))
if tot ==2:
    print('Ele É UM PRIMO')
else:
    print('Ele NÃO É PRIMO')