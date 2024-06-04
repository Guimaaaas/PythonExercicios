print('==============================')
print('    10 TERMOS DE UMA PA')
print('==============================')
num = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
for c in range(0,10):
    print('{} '.format(num), end='-> ')
    num += razao
print('ACABOU')