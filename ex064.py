num = 0
som = 0
total = 0
while num != 999:
    num = int(input('Digite um número [999 para parar]: '))
    if num == 999:
        break
    som += num
    total += 1
print(f'Você digitou {total} números e a soma entre eles foi {som}.')