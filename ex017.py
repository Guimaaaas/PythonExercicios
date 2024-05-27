import math
oposto = float(input('Digite o valor do cateto oposto: '))
adjacente = float(input('Digite o valor do cateto adjacente: '))
print('O valor da hipotenusa desse triâmgulo é {:.2f}'.format(math.hypot(oposto, adjacente)))

