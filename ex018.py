import math
ang = float(input('Digite o ângulo que você deseja: '))
seno = math.sin(math.radians(ang))
coseno = math.cos(math.radians(ang))
tang = math.tan(math.radians(ang))
print('O seno de {} é {:.2f}'.format(ang, seno))
print('O coseno de {} é {:.2f}'.format(ang, coseno))
print('O tang de {} é {:.2f}'.format(ang, tang))
