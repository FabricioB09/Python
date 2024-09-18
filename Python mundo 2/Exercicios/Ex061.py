print('=' * 30)
print('    10 TERMOS DE UMA P.A')
print('=' * 30)
Primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
termo = Primeiro
cont = 1
while cont <= 10:
    print(termo, end=' -> ')
    termo = termo + razao
    cont = cont + 1
print('ACABOU')