'''import math
c_op = float(input('Comprimento do cateto oposto: '))
c_ad = float(input('Comprimento do cateto adjacente: '))
hip = math.sqrt((math.pow(c_op,2)+math.pow(c_ad,2)))
print('A hipotenusa vai medir: {:.2f} '.format(hip))'''

from math import hypot
c_op = float(input('Comprimento do cateto oposto: '))
c_ad = float(input('Comprimento do cateto adjacente: '))
hip=hypot(c_op,c_ad)
print('A hipotenusa vai medir: {:.2f}'.format(hip))