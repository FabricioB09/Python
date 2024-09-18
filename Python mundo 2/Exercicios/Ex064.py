num = 0
cont = 0
tot = 0
while num != 777:
    num = int(input('Digite um numero: [Digite 777 para parar]'))
    if num != 777:   
        tot = tot + num
        cont = cont + 1
print('Foram digitados {} numeros e a soma deles é {}'.format(cont, tot))