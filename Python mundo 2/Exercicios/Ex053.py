frase = str(input('Digite uma Frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto) -1, -1, -1):
    inverso = inverso + junto[letra]
print('O iverso de {} é {}'.format(junto, inverso))
if inverso == junto:
    print('Temos um Palindromo')
else:
    print('a frase digitada não é um Palindromo')