cores = {'limpa':'\033[m',
         'azul':'\033[0;34m',
         'amarelo':'\033[33m',
         'verde':'\033[32m',
         'vermelho':'\033[31m',
         'pretoebranco':'\033[7;30m'}

num = int(input('Primeiro valor: '))
num2 = int(input('Segundo valor: '))
num3 = int(input('Terceiro valor: '))
menor = num

if menor > num2:
    menor = num2
if menor > num3:
    menor = num3
maior = num
if maior < num2:
    maior = num2
if maior < num3:
    maior = num3

print('O menor valor digitado foi {}{}{}'.format(cores['amarelo'], menor, cores['limpa']))
print('O maior valor digitado foi {}{}{}'.format(cores['amarelo'], maior, cores['limpa']))


###numeros = [num,num2,num3]
###numeros.sort()
###print('O menor valor digitado foi {}'.format(numeros[0]))
###print('O maior valor digitado foi {}'.format(numeros[2]))


