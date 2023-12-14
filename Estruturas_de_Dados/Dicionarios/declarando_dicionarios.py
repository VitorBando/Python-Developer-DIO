pessoa = {'nome': 'Vitor', 'idade': 24}

pessoa = dict(nome='Vitor', idade=24)

pessoa['telefone'] = '3333-1234'

print(pessoa['nome'])
print(pessoa['idade'])
print(pessoa['telefone'])

dados = {'nome': 'Vitor', 'idade': 24, 'telefone': '3333-1234'}

print(dados['nome'])
print(dados['idade'])
print(dados['telefone'])

dados['nome'] = 'Beatriz'
dados['idade'] = 22
dados['telefone'] = '5048-2006'

print(dados['nome'])
print(dados['idade'])
print(dados['telefone'])


contatos = {
    'joao@gmail.com': {'nome': 'Joao', 'telefone': '3332-1112'},
    'maria@gmail.com': {'nome': 'Maria', 'telefone': '3331-2223'},
    'jose@gmail.com': {'nome': 'Jose', 'telefone': '3330-3334'},
    'guilhermina@gmail.com': {'nome': 'Guilhermina', 'telefone': '2229-4445'},

}

print(contatos['maria@gmail.com']['nome'])
print(contatos['maria@gmail.com']['telefone'])

for chave in contatos:
    print(chave, contatos[chave])


for chave, valor in contatos.items():
    print(valor, chave)