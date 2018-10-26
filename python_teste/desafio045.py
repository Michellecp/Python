from random import randint
from time import sleep
itens=('Pedra', 'Papel', 'Tesoura')
computador= randint(0,2)

print('{:-^40}'.format('VAMOS JOGAR'))
print('''Suas Opções:
[0] PEDRA
[1] PAPEL
[2] TESOURA''')
jogador=int(input('Qual a sua jogada? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')

print('-='*14)
print('COMPUTADOR jogou {}'.format(itens[computador]))
print('JOGADOR jogou {}'.format(itens[jogador]))
print('-='*14)

if computador==0: #computador jogou Pedra
    if jogador==0:
        print('EMPATE')
    elif jogador==1:
        print('\33[30m JOGADOR VENCE')
    elif jogador==2:
        print('COMPUTADOR VENCE')
    else:
        print('Jogada Inválida')

elif computador==1: #computador jogou Papel
    if jogador==0:
        print('COMPUTADOR VENCE')
    elif jogador==1:
        print('EMPATE')
    elif jogador==2:
        print('\33[30m JOGADOR VENCE')

    else:
        print('Jogada Inválida')

elif computador==2: #computador jogou Tesoura
    if jogador==0:
        print('\33[30m JOGADOR VENCE')
    elif jogador==1:
        print('COMPUTADOR VENCE')
    elif jogador==2:
        print('EMPATE')
    else:
        print('Jogada Inválida')

else:
    print('Jogada Inválido')