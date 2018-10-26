from math import radians,sin,cos,tan
ang = float(input('Digite o angulo que você deseja: '))
print('O angulo {} tem o SENO de {:.2f}'.format(ang, sin(radians(ang))))
print('O angulo {} tem o COSSENO de {:.2f}'.format(ang, cos(radians(ang))))
print('O angulo {} tem a TANGENTE de {:.2f}'.format(ang, tan(radians(ang))))