import random
from time import sleep
num = random.randint(0,5)
print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
print('Vou pensar em um número entre 0 e 5. Tente Adivinhar...')
print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
chute = int(input('Em qual número eu pensei?: '))
print('PROCESSANDO...')
sleep(2)
if chute == num:
    print('VOCÊ ACERTOU!!!!')
else:
    print('ERROOOUUUUUUU!!!')
    print('O número era {}'.format(num))
