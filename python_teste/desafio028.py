from random import randint
from  time import  sleep

print('-*-' * 20)
print('Vou pensar em umk numero entre 0 e 5. Tente advinhar...')
print('-*-' * 20)

num1=str(input('Digite um numero:'))

print('Processando...')
sleep(3)

num = randint(0,5) #verifica se um numero aleatório de 0 a 5

if num1 != num:
   print('GANHEI! Eu pensei no numero {} e não no {}'.format(num, num1))
else:
    print('PARABENS! Você conseguiu me vencer')
