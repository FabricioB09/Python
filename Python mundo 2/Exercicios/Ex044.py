print('{:=^40}'.format('INOVE TECH GRAFICA RAPIDA'))
preco = float(input('Preço das compras: R$ '))
print('FORMAS DE PAGAMENTOS')
print('[1] Á VISTA DINHEIRO OU CHEQUE')
print('[2] Á VISTA NO CARTÃO DE CREDITO/DEBITO')
print('[3] 2X NO CARTÃO')
print('[4] 3X OU MAIS NO CARTÃO')
opção = int(input('Qual a opção? '))
if opção == 1:
    total = preco - (preco * 10 / 100)
elif opção == 2:
    total = preco - (preco * 5 / 100)
elif opção == 3:
    total = preco
    parc = total / 2
    print('Sua compra de {}R$ vai custar {}R$ no final parcelado em 2x de {}R$'.format(preco, total, parc ))
elif opção == 4:
    total = preco + (preco * 20 / 100) 
    totparc = int(input('Quantas Parcelas?'))
    parc = total / totparc
    print('Sua compra de {}R$ vai custar {}R$ no final parcelado em {}x de {}R$'.format(preco, total, totparc, parc ))
else:
    total = 0
    print('OPÇÃO INVALIDA! tente novamente')    
print('Sua compra de {}R$ vai custar {}R$ no final'.format(preco, total))