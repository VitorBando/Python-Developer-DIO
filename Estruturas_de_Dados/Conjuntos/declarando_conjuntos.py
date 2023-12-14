inteiro_unico = set([1, 2, 3, 1, 3, 4])
print(inteiro_unico)

char_unico = set('abacaxi')
print(char_unico)

carro_unico = set(('palio', 'gol', 'celta', 'palio',))
print(carro_unico)

for  carro in carro_unico:
    print(carro)

for indice, carro in enumerate(carro_unico):
    print(f'{indice}: {carro}')    

linguagens = {'python', 'java', 'python'}
print(linguagens)

numeros = {1, 2, 3, 2}
numeros = list(numeros)
print(numeros[0])
