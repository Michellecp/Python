
print('='*8)
print('10 TERMOS DE UMA PA')
print('='*8)

p_termo=int(input('Primeiro Termo: '))
r= int(input('RAZÃO: '))
decimo=p_termo+(10-1)*r

for c in range (p_termo,decimo+r,r):
      print('{} '.format(c), end= '->')
print('ACABOU')