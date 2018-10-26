largura=float(input('Digite a largura da parede:'))
altura=float(input('Digite a altura da parede:'))
area =largura*altura
tinta = area/2
print('Sua parede tem dimenção de {}x{} e a sua área é {:.2f}'.format(largura,altura, area))
print('Para pintar essa parede você precisará de {:.2f}'.format(tinta))