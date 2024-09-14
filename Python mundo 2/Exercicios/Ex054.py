from datetime import date
atual = date.today().year
totmaior = 0
totmenor = 0
for pess in range(1, 7):
    nasc = int(input('Em que ano a {} pessoa nasceu? '.format(pess)))
    idade = atual - nasc
    if idade >= 21:
        totmaior = totmaior + 1
    else:
        totmenor = totmenor + 1
print('Das pessoas digitadas {} são maiores e {} são menores de idade.'.format(totmaior, totmenor))