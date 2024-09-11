casa = float(input('Qual o valor da casa(R$)? '))
salario = float(input('Qual o seu salario(R$)?'))
anos = float(input('Quantos anos de financiamento? '))
prestação = casa / (anos * 12)
minimo = salario * 30/100
print('Para pagar uma casa de R${:.2f} em {:.0f} anos a prestação será de R${:.2f}'.format(casa, anos, prestação))
if prestação <= minimo:
    print('O empréstimo pode ser CONCEDIDO, PARABÉNS!')
else:
    print('Empréstimo NEGADO!')