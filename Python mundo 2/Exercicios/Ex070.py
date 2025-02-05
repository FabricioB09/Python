total = tot1000 = menor = cont = 0
barato = ' '
while True:
    produto = str(input('Nome do produto: '))
    preço = float(input('Preço: R$'))
    cont += 1
    total += preço
    if preço > 1000:
        tot1000 += 1
    if cont == 1 :
        menor = preço
        barato = produto
    else:
       if preço < menor:
           menor = preço
           barato = produto 
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if resp == 'N':
        break
print('{:-^40}'.format('FIM DO PROGRAMA'))
print(f'O total das compras foi: {total:.2f}R$')
print(f'Temos {tot1000} produto custando 1000R$ ou mais.')
print(f'O produto mais barato é {barato} e custa {menor:.2f}R$')