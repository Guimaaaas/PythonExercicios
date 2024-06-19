n = s = c = 0

while n != 999:
    n = int(input('Digite um valor: '))
    if n == 999:
        break
    c += 1
    s += n
print(f'A soma dos {c} valores foi {s}!')