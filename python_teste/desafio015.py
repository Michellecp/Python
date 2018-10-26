qtd_km=float(input('Qual a quantidade de km percorrido? '))
qtd_dias=int(input('Por qtos dias foi aluguel?'))
preco_pagar= (qtd_km* 0.15)+(qtd_dias*60)
print('Total a pagar é R$ {:.2f}'.format(preco_pagar))