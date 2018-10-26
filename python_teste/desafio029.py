vel=float(input('Digite a velocidade atual do carro:'))
if vel > 80 :
    print('MULTADO! Você excedeu o limite de velocidade permitido que é de 80km/h')
    print('Você deve paga uma multa de R$ {:.2f}'.format((vel-80.0)*7.00))

print('Tenha um Bom Dia! Dirija com segurança!')