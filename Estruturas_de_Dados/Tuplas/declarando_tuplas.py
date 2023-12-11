frutas = ('larana', 'pera', 'uva',)
print(frutas[0])
print(frutas[-1])

letras = tuple('python')
print(letras[2:])
print(letras[:2])
print(letras[1:3])
print(letras[0:3:2])

numeros = tuple([1, 2, 3, 4])

pais = ('Brasil',)

matriz = (
    (1, 'a', 2),
    ('b', 3, 4),
    (6, 5, 'c'),
)

print(matriz[0])
print(matriz[0][0])
print(matriz[-1])
print(matriz[-1][-1])

carros = ('gol', 'celta', 'palio',)

for carro in carros:
    print(carro)

for indice, carro, in enumerate(carros):
    print(f'{indice}: {carro}')
