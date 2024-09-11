peso = float(input('Qual o seu peso (KG)? '))
altura = float(input('Qual a sua altura? ' ))
imc = peso / (altura ** 2)
print('O seu IMC é igual a {:.1f}'.format(imc))
if imc < 18.5:
    print('Você esta ABAIXO DO PESO, cuidado!')
elif 18.5 <= imc < 25:
    print('Você esta no PESO IDEAL, Parabéns!')
elif  25 <= imc < 30:
    print('Você esta em SOBREPESO')
elif 30 <= imc < 40:
    print('Você esta em OBESIDADE')
else:
    print('Você esta em OBESIDADE MORBIDA, CUIDADO!')
