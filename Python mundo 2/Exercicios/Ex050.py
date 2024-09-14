soma = 0
cont = 0
for c in range(1,7):
    num = int(input('Digite O {} valor: '.format(c)))
    if num % 2 == 0:
        soma = soma + num
        cont = cont + 1
print('Você informou {} numeros pares, e a soma de todos eles foi {}'.format(cont, soma))