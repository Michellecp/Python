
frase=str(input('Digite uma frase: ')).strip().upper()
palavra=frase.split()
junto= ''.join(palavra)
inverso = ''
inverso=junto[::-1]
'''for letra in range (len(junto) -1, -1, -1):
    inverso+=junto[letra]'''
print('O inverso de {} é {}'.format(junto, inverso))
if inverso==junto:
    print('Temos um Palíndromo')
else:
    print('A frase digitada Não é Palíndromo')


