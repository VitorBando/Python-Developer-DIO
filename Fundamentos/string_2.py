nome = 'Vitor'
idade = 24
profissao = 'Analista'
linguaguem = 'Sql'
saldo = 45.435

dados = {'nome':'Vitor','idade':24}

print('Nome: %s Idade: %d' %(nome, idade))

print('Nome: {} Idade: {}'.format(nome, idade))
print('Nome: {0} Idade: {1} Nome: {0}'.format(nome, idade))
print('Nome: {nome} Idade: {idade} Nome: {nome}'.format(nome=nome, idade=idade))
print('Nome: {nome} Idade: {idade}'.format(**dados))

print(f'Nome: {nome} Idade: {idade}')
print(f'Nome: {nome} Idade: {idade} Saldo: {saldo:.2f}')