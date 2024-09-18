from time import sleep
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
opção = 0
while opção != 5:
    print('''
      [1] Somar
      [2] Multiplicar
      [3] Maior valor
      [4] Novos números
      [5] Sair do programa
    ''')
    opção = int(input('Qual é a sua opção? '))
    if opção == 1:
        soma = n1 + n2
        print('A soma entre {} e {} é igual a {}'.format(n1, n2, soma))
    elif opção == 2:
        multi = n1 * n2
        print('O resultado de {} x {} é igual a {}'.format(n1, n2, multi))
    elif opção == 3:
        if n1 > n2:
            maior = n1
            print('Entre {} e {} o maior é {}'.format(n1, n2, maior))
        elif n2 > n1:
            maior = n2
            print('Entre {} e {} o maior é {}'.format(n1, n2, maior))
        else:
            print('Os numeros são Iguais')
    elif opção == 4:
        print('Digite os novos valores: ')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif opção == 5:
        print('Finalizando...')
    else:
        print('Opção Invalida! Tente novamente')
    print('=-=' * 20)
    sleep(1)
print('Fim do Programa')