tab=total=cont=0

while True:
    print('---'*8)
    tab = int(input('Quer ver a Tabuada de qual valor: '))
    print('---'*8)
    if tab < 0:
        break
    for cont in range (1,11):
        total=tab*cont
        print(f'{tab}x{cont} = {total}')
print('PROGRAMA TABUADA ENCERRADO. VOLTE SEMPRE!')


