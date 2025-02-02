
while True:
    print('DIGITE 0 PARA PARAR!')
    n = int(input('Quer ver a tabuada de qual valor?'))
    print('-' * 30)
    if n == 0:
        break
    for c in range(1, 11):
        print(f'{n} x {c} = {n*c}')
    print('-' * 30)
print('Programa Tabuada encerrado, VOLTE SEMPRE!')