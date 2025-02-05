print('='*30)
print('{:^30}'.format('FB BANK'))
print('='*30)
valor = int(input('Qual valor que você deseja sacar? R$'))
total = valor
ced = 100
totced = 0
while True:
    if total >= ced:
        total = total - ced
        totced += 1
    else:
       if totced > 0:
            print(f'O total de cedulas de {ced}R$ foi de {totced} cedulas')
       if ced == 100:
           ced = 50
       elif ced == 50:
           ced = 20
       elif ced == 20:
           ced = 10
       elif ced == 10:
           ced  = 5
       elif ced == 5:
           ced = 2 
       totced = 0 
       if total == 0:
           break
print('='* 30)
print('{:^30}'.format('Volte sempre ao FB BANK'))