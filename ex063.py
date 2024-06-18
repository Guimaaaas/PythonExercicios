print('-----------------------------------')
print('Sequência de Fibonacci')
print('-----------------------------------')
qtd = int(input('Quantos termos você quer mostrar: '))
while qtd <= 0:
    qtd = int(input('Por favor, insira um número positivo: '))
cont = 2
fib = [0,1]
print('{} -> {}'.format(fib[0],fib[1]), end=' -> ')
while cont < qtd:
    num = fib[cont-2] + fib[cont-1]
    print('{}'.format(num), end=' -> ')
    fib.append(num)
    cont += 1
print('FIM')
