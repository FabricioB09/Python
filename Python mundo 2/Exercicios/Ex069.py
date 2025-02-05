tot18 = totm = tot20 = 0
while True:
   idade = int(input('Idade: '))
   sexo = ' ' 
   while sexo not in 'MF':
      sexo = str(input('Sexo [M/F]: ')).strip().upper()[0]
   if idade >= 18:
      tot18 += 1
   if sexo == 'M':
      totm += 1
   if sexo == 'F' and idade <= 20:
      tot20 += 1   
   resp = ' '
   while resp not in 'SN':
      resp = str(input('Quer continuar? [S/N]')).strip().upper()[0]
   if resp == 'N':
      break 
print('Acabou')
print(f'Total de pessoas com mais de 18 Anos: {tot18}')
print(f'Ao todo temos {totm} homens cadastrados')
print(f'E temos {tot20} mulheres com idade igual ou inferior a 20 Anos.')