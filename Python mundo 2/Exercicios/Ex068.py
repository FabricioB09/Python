from random import randint
v = 0
while True:
    jogador = int(input('Digite um valor: '))
    computador = randint(0,10)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PpIi':
        tipo = str(input('Par ou Impar?')).strip().upper()[0]
    print(f'Você jogou {jogador} e o computador jogou {computador}, e o total foi {total}' ,end=' ')
    print('Deu PAR' if total % 2 == 0 else 'Deu IMPAR')
    if tipo == 'P':
        if total % 2 == 0:
            print('Você venceu!')
            v += 1
        else:
            print('Você Perdeu!')
            break
    elif tipo == 'I':
        if total % 2 == 0:
            print('Você Venceu!')
            v += 1
        else:
            print('Você Perdeu!')
            break
print(f'GAME OVER você venceu {v} vezes')