from random import randint
tentativas = 0
acertou = False
random = randint(0,10)
print('''Sou seu computador...
Acabei de pensar em um número entre 0 e 10.
Será que você consegue adivinhar qual foi?''')
while not acertou:
    tentativa = int(input('Digite sua tentativa: '))
    tentativas += 1
    if tentativa > random:
        print('Menos... tente mais uma vez!')
    elif tentativa < random:
        print('Mais... tente mais uma vez!')
    else:
        acertou = True
print('Você acertou com {} tentativas. Parabéns!'.format(tentativas))
