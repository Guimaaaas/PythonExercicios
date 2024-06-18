r = True
total = 0
soma = 0
maior = 0
menor = 0
while r:
    num = int(input('Digite um número: '))
    total += 1
    if maior == 0 and menor == 0:
        maior = num
        menor = num
    elif num > maior:
        maior = num
    elif num < menor:
        menor = num
    soma += num
    resp = input('Quer continuar [S/N]: ')
    while resp not in 'SsNn':
        resp = input('Comando inválido! Quer continuar [S/N]: ')
    if resp in 'Nn':
        break
print(f'Você digitou {total} números e a média foi {soma/total:.2f}')
print(f'O maior valor foi {maior} e o menor foi {menor}')
