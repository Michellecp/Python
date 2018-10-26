peso = float(input('Digite o seu peso:'))
altura = float(input('Digite a sua altura: '))

def imc (peso, altura): #função que calcula o IMC
     return (peso / (altura ** 2))

def avaliar_imc(indice):
    if indice < 20:
         result= 'CUIDADO!Abaixo do Peso'
    elif indice <= 24.9:
        result= 'PARABÉNS! O seu peso esta normal!'
    elif indice <= 29.9:
        result='CUIDADO! você esta em SOBREPESO'
    else:
     result ='CUIDADO. Você esta em OBESIDADE!'

print('O seu IMC é {:.2f}\n {}'.format(imc(peso,altura),avaliar_imc()))