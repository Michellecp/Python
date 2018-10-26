viagem=float(input('Qual a distancia da sua viagem?'))
print('Você esta prestes a começar uma viagem de {} km '.format(viagem))
if viagem <= 200 :
    print('E o preço da sua passagem é R$ {:.2f}'.format(viagem*0.50))
else:
    print('E o preço da sua passagem é R$ {:.2f}'.format(viagem*0.45))