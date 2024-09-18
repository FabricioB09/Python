print('=' * 30)
print('     TERMOS DE UMA P.A')
print('=' * 30)
Primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
termo = Primeiro
total = 0
cont = 1
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print(termo, end=' -> ')
        termo = termo + razao
        cont = cont + 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais? '))
print('Progressão finalizada com {} termos mostrados'.format(total))