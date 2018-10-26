print('{:=^40}'.format('LOJAS PACHECO'))

compra=float(input('Preço da Compra R$ '))

print('''FORMAS DE PAGAMENTO
[1] à vista dinheiro/cheque
[2] à vista no cartão
[3] 2x no cartão
[4] 3x ou mais no cartão''')

opcao=float(input('Opção de Pagamento: '))

if opcao==1:
    print('Sua compra de R$ {} vai custar R$ {} no final'.format(compra, compra-(compra*10/100)))
elif opcao==2:
    print('Sua compra de R$ {} vai custar R$ {} no final'.format(compra, compra-(compra*5/100)))
elif opcao==3:
    print('Sua compra de será parcelada em 2 vezes de {}'.format(compra/2))
elif opcao==4:
    parcelas=int(input('Quantas parcelas?'))
    total=compra+(compra*20/100)
    print('Sua compra será parcelada em {}x de {:.2f} COM JUROS'.format(parcelas, total/parcelas))
    print('Sua compra de {:.2f} vai custar {:.2f} no final'.format(compra, total))
else:
    print('\33[31m Opção invalida de pagamento. Tente novamente.')