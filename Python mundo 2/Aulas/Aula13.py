for c in range(10,0, -1):
    print(c)
print('FIM')
print('-=' * 10)
n = int(input('Digite um numero: '))
for c in range(0,n+1):
    print(c)
print('FIM')
print('-=' * 10)
s = 0
for c in range(0,3):
    n = int(input('Digite um numero: '))
    s = s + n
print('A soma de todos os valores digitados é {}'.format(s))