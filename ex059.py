a = int(input('Primeiro valor: '))
b = int(input('Segundo valor: '))
while True:
    print('''    [ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] novos números
    [ 5 ] sair do programa''')
    escolha = int(input('>>>>> Digite sua opção: '))
    if escolha == 1:
        print('A soma entre {} + {} = {}'.format(a,b,a+b))
        print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
    elif escolha == 2:
        print('A multiplicação entre {} * {} = {}'.format(a,b,a*b))
        print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
    elif escolha == 3:
        if a > b:
            print('{} é maior que {}'.format(a,b))
            print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
        elif a < b:
            print('{} é maior que {}'.format(b, a))
            print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
        else:
            print('Os números são iguais!')
            print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
    elif escolha == 4:
        a = int(input('Primeiro valor: '))
        b = int(input('Segundo valor: '))
        print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
    elif escolha == 5:
        break
    else:
        print('Opção inválida! Tente novamente')
        print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
