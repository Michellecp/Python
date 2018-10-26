from random import randint
computador= randint(0,10)
cont=0

print('-*-' * 20)
print('\033[31mSou o seu computador...\033[m')
print('Acabei de pensar em um numero entre 0 e 10.','\nSerá que você consegue advinhar qual foi?')
print('-*-' * 20)

acertou=False

while not acertou:
    jogador = int(input('Qual o seu palpite?'))
    cont+=1
    if jogador > computador:
        print('Menos...Tente mais uma vez!')
    elif jogador <computador:
        print('Mais...Tente mais uma vez')
    elif computador == jogador:
        acertou= True

print('Acertou com {} tentativas. Parabéns!!'.format(cont))


