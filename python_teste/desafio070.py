result=''
preco=cont=menor=val_men=total=n=0

while True:
    if result == 'N':
        break
    print('---' * 10)
    print('LOJAS SUPER BARATÃO')
    print('---' * 10)
    prod=str(input('Nome do Produto: '))
    preco=float(input('Preço: '))
    result=str(input('Quer continuar?[S/N]')).strip().upper()
    total += preco
    menor=preco
    if preco> 1000.00:
        cont+=1
    if preco > menor:
        val_men=preco
        n=prod
print('FIM DO PROGRAMA')
print(f'''O total da compra foi: {total}
Temos {cont} custando mais que R$ 1000.00
O produto mais barato foi uma {n} que custa R$ {val_men}''')
