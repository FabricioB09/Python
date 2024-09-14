somidade = 0
mediaidade = 0
maioridadehomem = 0
nomevelho = ''
totfem = 0
totfem20 = 0
for p in range(1, 5):
    print('-----{} PESSOA------'.format(p))
    nome = str(input('Nome: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    idade = int(input('Idade: '))
    somaidade = somidade + idade
    if p == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomevelho = nome
    if idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Ff':
        totfem = totfem + 1
    if sexo in 'Ff' and idade > 20:
        totfem20 = totfem20 + 1
mediaidade = somaidade / 4
print('A média de idade do grupo é de {} anos'.format(mediaidade))
print('O homem mais velho tem {} anos e o seu nome é {}'.format(maioridadehomem,nomevelho))
print('O total de mulheres foi {}, e as acima dos 20 anos foi {}'.format(totfem, totfem20))
 