contatos = {
    'joao@gmail.com': {'nome': 'Joao', 'telefone': '3332-1112'},
    'maria@gmail.com': {'nome': 'Maria', 'telefone': '3331-2223'},
    'jose@gmail.com': {'nome': 'Jose', 'telefone': '3330-3334'},
    'guilhermina@gmail.com': {'nome': 'Guilhermina', 'telefone': '2229-4445'},

}

contatos.clear()
print(contatos)

contatos = {
    'joao@gmail.com': {'nome': 'Joao', 'telefone': '3332-1112'},
}

copia = contatos.copy()
copia['joao@gmail.com'] = {'nome': 'Joaozin'}

print(contatos['joao@gmail.com'])
print(copia['joao@gmail.com'])

print(dict.fromkeys(['nome', 'telefone']))

print(dict.fromkeys(['nome', 'telefone'], 'vazio'))


# print(contatos['chave'])
print(contatos.get('chave'))
print(contatos.get('chave', {}))
print(contatos.get('joao@gmail.com', {}))

print(contatos.items())
print(contatos.keys())


print(contatos.pop('joao@gmail.com'))

print(contatos.pop('joao@gmail.com', {}))

contatos = {
    'joao@gmail.com': {'nome': 'Joao', 'telefone': '3332-1112'},
}

print(contatos.popitem())

contato = {'nome': 'Joao', 'telefone': '3332-1112'}

contato.setdefault('nome', 'Beatriz')
print(contato)

contato.setdefault('idade', 28)
print(contato)


contatos = {
    'joao@gmail.com': {'nome': 'Joao', 'telefone': '3332-1112'},
}

contatos.update({'joao@gmail.com': {'nome': 'Joaozin'}})
print(contatos)

contatos.update({'vitor@gmail.com': {'nome': 'Vitor', 'telefone': '6404-3128'}})
print(contatos)

contatos = {
    'joao@gmail.com': {'nome': 'Joao', 'telefone': '3332-1112'},
    'maria@gmail.com': {'nome': 'Maria', 'telefone': '3331-2223'},
    'jose@gmail.com': {'nome': 'Jose', 'telefone': '3330-3334'},
    'guilhermina@gmail.com': {'nome': 'Guilhermina', 'telefone': '2229-4445'},

}

print(contatos.values())

contatos = {
    'joao@gmail.com': {'nome': 'Joao', 'telefone': '3332-1112'},
    'maria@gmail.com': {'nome': 'Maria', 'telefone': '3331-2223'},
    'jose@gmail.com': {'nome': 'Jose', 'telefone': '3330-3334'},
    'guilhermina@gmail.com': {'nome': 'Guilhermina', 'telefone': '2229-4445'},

}

print('joao@gmail.com' in contatos)
print('vitor@gmail.com' in contatos)
print('idade' in contatos['joao@gmail.com'])
print('telefone' in contatos['guilhermina@gmail.com'])

del contatos['joao@gmail.com']['telefone']
del contatos['guilhermina@gmail.com']

print(contatos)
