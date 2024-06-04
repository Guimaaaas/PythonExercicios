import emoji
from random import randint
from time import sleep

jogadas = ('PEDRA 👊', 'PAPEL 🧻', 'TESOURA ✂')
comp = randint(0,2)
print('================ JO-KEN-PÔ ================')
print('Escolha sua Jogada')
print(emoji.emojize('[ 1 ] PEDRA 👊'))
print(emoji.emojize('[ 2 ] PAPEL 🧻'))
print(emoji.emojize('[ 3 ] TESOURA ✂'))
jogada = int(input('Opção: ')) - 1
if jogada < 0 or jogada > 2:
        print('JOGADA INVÁLIDA!!')
        exit()
print('JO')
sleep(0.7)
print('KEN')
sleep(0.7)
print('PÔ!!!')
sleep(0.2)
print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
print(emoji.emojize('O computador escolheu {}'.format(jogadas[comp])))
print(emoji.emojize('Você escolheu {}'.format(jogadas[jogada])))
print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
if (jogada == 0 and comp == 2) or (jogada == 1 and comp == 0) or (jogada == 2 and comp == 1):
    print(emoji.emojize('VOCÊ VENCEU!!! 🔥🔥🔥'))
elif jogada == comp:
    print(emoji.emojize('EMPATE 🤝'))
else:
    print(emoji.emojize('COMPUTADOR VENCEU!!! 🤖🤖🤖'))