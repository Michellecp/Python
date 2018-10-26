n=soma=0
while True:
    n=int(input('Digite um numero:'))
    if n == 999:
        break
    soma+=n
#print('A soma é {}'.format(soma))
print(f'A soma e {soma}')