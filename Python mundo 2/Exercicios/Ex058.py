from random import randint
computador = randint(0, 10)
print('=' * 30)
print('     JOGO DA ADIVINHAÇÃO')
print('=' * 30)
print('Sou seu computador...')
print('Acabei de pensar um numero entre 0 e 10.')
print('Sera que você consegue advinhar qual é?')
acertou = False
palpites = 0
while not acertou:
    r = int(input('Qual o seu palpite? '))
    palpites += 1
    if r == computador:
        acertou = True
    else:
        if r < computador:
            print('Maior.. Tente novamente')
        else:
            print('Menor.. Tente novamente')
print('Acertou com {} tentativas, Parabéns!'.format(palpites))