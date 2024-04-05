largura = float(input('Digite a largura da parede: '))
altura = float(input('Digite a altura da parede: '))
area = largura*altura
print('Sua parede tem a dimensão de {}X{} e sua área é de {}m2.'.format(largura,altura,area))
print('Para pintar essa parede, você precisará de {}l de tinta.'.format(area/2))