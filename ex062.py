print('Gerador de PA')
print('-=-=-=-=-=-=-=-=-=-=-=-=-=-')
num = int(input('Primeiro termo: '))
raz = int(input('Razão da PA: '))
cont = 0
qtd = 10
termos = 0
while qtd != 0:
    while cont < qtd:
        print('{} -> '.format(num), end='')
        num += raz
        cont += 1
        termos += 1
    print('PAUSA')
    cont = 0
    qtd = int(input('Quantos termos você quer mostrar a mais: '))
print('Progressão finalizada com {} termos mostrados.'.format(termos))