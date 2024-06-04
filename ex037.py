num = int(input('Digite um número inteiro: '))
print('Escolha a base para qual deseja converte-lo')
print('[ 1 ] converter para \033[33mBINÁRIO\033[m')
print('[ 2 ] converter para \033[33mOCTAL\033[m')
print('[ 3 ] converter para \033[33mHEXADECIMAL\033[m')
escolha = int(input('Sua opção: '))
if escolha == 1:
    print('A representação em binário de {} é {}'.format(num, bin(num)[2:]))
elif escolha == 2:
    print('A representação em octal de {} é {}'.format(num, oct(num)[2:]))
elif escolha == 3:
    print('A representação em hexadecimal de {} é {}'.format(num, hex(num)[2:]))
else:
    print('Opção inválida')
