frase = input('Digite uma frase: ').strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = junto[::-1]
print('{} invertido é {}'.format(junto,inverso))

if junto == inverso:
    print('É palindromo')
else:
    print('NÃO é palindromo')