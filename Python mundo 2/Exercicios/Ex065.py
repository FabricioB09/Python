resp = 'S'
cont = 0
tot = 0
maior = 0
menor = 0
while resp in 'Ss':
    num = int(input('Digite um numero: '))
    cont = cont + 1
    tot = tot + num
    if cont == 1:
        maior = menor = num
    else: 
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    resp = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
media = tot / cont
print('Você digitou {} numeros e a media foi {}'.format(cont, media))
print('O maior valor foi {} e o menor valor foi {}'.format(maior, menor))