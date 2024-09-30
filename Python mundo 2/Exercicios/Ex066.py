s = 0
n = 0
c = 0
while True:
    n = int(input('Digite um valor (Digite 999 para parar): '))
    if n == 999:
        break
    s += n
    c += 1
print(f'a soma dos {c} numeros é igual a {s}')