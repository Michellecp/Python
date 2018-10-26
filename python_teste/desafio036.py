#Calculo de Emprestimo
print('*-*'*15, '\nBanco do Povo')
print('*-*'*15)
valor=float(input('Qual o valor do imóvel? R$ '))
salario=float(input('Qual o valor do seu salario? R$'))
tempo=int(input('Em quantas anos deseja pagar?'))

parcel=(valor/(tempo*12))

val_prest=salario/100*30
print('Para pagar uma casa de {} em {} anos será uma prestação de {:.2f}'.format(valor,tempo, parcel))

if val_prest <= parcel:
    print('Emprestimo NEGADO!!')
else:
    print('Emprestimo pode ser CONCEDIDO!!')