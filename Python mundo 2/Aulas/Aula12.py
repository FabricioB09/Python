nome = str(input('Qual o seu nome? '))
if nome == 'Fabricio':
    print('Seu nome é bonito')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo':
    print('Seu nome é bem popular no Brasil')
elif nome in 'Ana Claudia Juliana Cristiana':
    print('Que belo nome feminino!')
else:
    print('Que nome normal')
print('Tenha um bom dia, {}!'.format(nome))