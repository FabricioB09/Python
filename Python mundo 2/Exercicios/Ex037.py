numero = int(input('Digite um numero INTEIRO: '))
print('Escolha uma das bases para conversão:')
print('[1] CONVERTER PARA BINARIO')
print('[2] CONVERTER PARA OCTAL')
print('[3] CONVERTER PARA HEXADECIMAL')
opção = int(input('Sua opção: '))
if opção == 1:
    print('{} convertido para BINARIO é igual {}'.format(numero, bin(numero)[2:]))
elif opção == 2:
    print('{} convertido para OCTAL é igual a {}'.format(numero, oct(numero)[2:]))
elif opção == 3:
    print('{} convertido para HEXADECIMAL é igual a {}'.format(numero, hex(numero)[2:]))
else:
    print('Opção Invalida')

