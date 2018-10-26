peso=float(input('Qual é o seu peso?(kg)'))
altura=float(input('Qual é sua altura?(m)'))

imc=peso/(altura**2)
print('O IMC desta pessoa é: {:.1f}'.format(imc))

if imc < 18.5:
    print('ATENÇÃO! Você esta na faixa de ABAIXO DO PESO')
elif 18.5<= imc <25:
    print('PARABÉNS! Você esta na faixa de PESO NORMAL')
elif 25<= imc <30:
    print('CUIDADO! Você esta na faixa de SOBREPESO')
elif 30<= imc < 40:
    print('CUIDADO! Você esta na faixa de OBESIDADE')
else:
    print('CUIDADO! Você esta na faixa de OBESIDADE MORBIDA')
