from random import randint
from time import sleep
itens = ('PEDRA' , 'PAPEL', 'TESOURA')
computador = randint(0, 2)
print('Suas opções: ')
print('[0] PEDRA')
print('[1] PAPEL')
print('[2] TESOURA')
jogador = int(input('Qual é a sua jogada? '))
print('-=' * 15)
print('JO')
sleep(0.7)
print('KEN')
sleep(0.7)
print('PO!!!')
sleep(0.7)
print('-=' * 15)
print('-=' * 15)
print('Computador jogou {}'.format(itens[computador]))
print('Jogador jogou {}'.format(itens[jogador]))
print('-=' * 15)
if  computador == 0:
    if jogador == 0:
        print('RESULTADO: EMPATE')
    elif jogador == 1:
        print('RESULTADO: JOGADOR VENCEU')
    elif jogador == 2:
        print('RESULTADO: COMPUTADOR VENCEU')
    else:
        print('RESULTADO: JOGADA INVALIDA')
elif computador == 1:
    if jogador == 0:
        print('RESULTADO: COMPUTADOR VENCEU')
    elif jogador == 1:
        print('RESULTADO: EMPATE')
    elif jogador == 2:
        print('RESULTADO: JOGADOR VENCEU')
    else:
        print('RESULTADO: JOGADA INVALIDA')
elif computador == 2:
    if jogador == 0:
        print('RESULTADO: JOGADOR VENCEU')
    elif jogador == 1:
        print('RESULTADO: COMPUTADOR VENCEU')
    elif jogador == 2:
        print('RESULTADO: EMPATE')
    else:
        print('RESULTADO: JOGADA INVALIDA')
