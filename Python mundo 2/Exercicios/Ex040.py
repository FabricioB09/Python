n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
media = (n1+n2)/2
if media >= 6:
    print('A media do aluno foi igual a {} e ele esta APROVADO'.format(media))
elif media >= 5:
    print('A media do aluno foi igual a {} e ele esta de RECUPERAÇÃO'.format(media))
else:
    print('A media do aluno foi igual a {} e ele esta REPROVADO'.format(media))