from random import randint

randnum = randint(0,10)
vitorias = 0

print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
print('VAMOS JOGAR PAR OU ÍMPAR')
while True:
    print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
    num = int(input('Diga um valor: '))
    escolha = input('Par ou Ímpar [P/I]: ')
    while escolha not in 'PpIi':
        print('Escolha inválida!! Tente Novamente')
        escolha = input('Par ou Ímpar [P/I]: ')
    print('----------------------------------------')
    print('Você jogou {} e o computador {}. Total de {} DEU {}'.format(num,randnum,num+randnum,'PAR' if (randnum + num)%2 == 0 else 'ÍMPAR'))
    if escolha in 'Pp' and (randnum + num)%2 == 0:
        print('VOCÊ VENCEU!!!')
        vitorias += 1
    elif escolha in 'Ii' and (randnum + num)%2 == 1:
        print('VOCÊ VENCEU!!!')
        vitorias += 1
    else:
        print('VOCÊ PERDEU!!!')
        break
print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
print(f'GAMEOVER! Você venceu {vitorias} vezes.')
