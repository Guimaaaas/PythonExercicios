print('Gerador de PA')
print('-=-=-=-=-=-=-=-=-=-=-=-=-=-')
num = int(input('Primeiro termo: '))
raz = int(input('Razão da PA: '))
cont = 1
while cont < 11:
    print('{} -> '.format(num), end='')
    num += raz
    cont += 1
print('FIM')
