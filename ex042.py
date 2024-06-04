cores = {'limpa':'\033[m',
         'azul':'\033[0;34m',
         'amarelo':'\033[33m',
         'verde':'\033[32m',
         'vermelho':'\033[31m',
         'pretoebranco':'\033[7;30m'}

print('-=-' * 10)
print('Analisador de Triângulos')
print('-=-' * 10)

r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))

if (r1 < r2 + r3) & (r2 < r1 + r3) & (r3 < r2 + r1):
    if r1 == r2 == r3:
        print('Os segmentos acima {}PODEM FORMAR{} um triângulo {}EQUILÁTERO!{}'.format(cores['verde'], cores['limpa'], cores['verde'], cores['limpa']))
    elif (r1 == r2 and r2 != r3) or (r2 == r3 and r3 != r1) or (r1 == r3 and r1 != r2):
        print('Os segmentos acima {}PODEM FORMAR{} um triângulo {}ISÓSCELES!{}'.format(cores['verde'], cores['limpa'], cores['verde'], cores['limpa']))
    else:
        print('Os segmentos acima {}PODEM FORMAR{} um triângulo {}ESCALETO!{}'.format(cores['verde'], cores['limpa'], cores['verde'], cores['limpa']))
else:
    print('Os segmentos acima {}NÃO PODEM FORMAR{} um triângulo!'.format(cores['vermelho'],cores['limpa']))
