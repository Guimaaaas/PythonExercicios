num = int(input('Digite um número: '))
total = 0
for c in range(1,num + 1):
    if num % c == 0:
        print('\033[33m', end='')
        total += 1
    else:
        print('\033[31m', end='')
    print('{} '.format(c), end='')
print('\033[m\nO número {} foi divisível {} vezes'.format(num,total))
if total < 3:
    print('Logo ele \033[32mÉ\033[m Primo!!')
else:
    print('Logo ele \033[31mNÃO\033[m é Primo!!')
