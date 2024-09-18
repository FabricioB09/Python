sexo = str(input('Informe seu Sexo: [M/F] ')).strip().upper()[0]
while sexo not in 'MmFf':
    sexo= str(input('Dados Invalidos. Informe seu Sexo: [M/F] ')).strip().upper()[0]
print('Sexo {} registrado com sucesso!'.format(sexo))