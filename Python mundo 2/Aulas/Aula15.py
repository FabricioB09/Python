n = 0
s = 0
while True:
    n = int(input('Digite um numero: '))
    if n == 999:
        break
    s = s + n
print(f'A soma dos numeros digitados é igual a: {s}')

#ultilizei a fstring no comando print para substituir o .format