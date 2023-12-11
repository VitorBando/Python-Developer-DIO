frutas = ['laranja', 'maca', 'uva']
print(frutas)

frutas = []
print(frutas)

letras = list('Python')
print(letras)

numeros = list(range(10))
print(numeros)

carro = ['Ferrari', 'F8', 4200000, 2020, 2900, 'Sao Paulo', True]
print(carro)

frutas = ['maca', 'laranja', 'uva', 'pera']
print(frutas[2])
print(frutas[-1])

matriz = [
    [1, 'a', 2],
    ['b', 3, 4],
    [6, 5, 'c']
]

print(matriz[0])
print(matriz[0][0])
print(matriz[0][-1])
print(matriz[-1][-1])


lista = ['p', 'y', 't', 'h', 'o', 'n']

print(lista[2:])
print(lista[:2])
print(lista[1:3])
print(lista[0:3:2])
print(lista[::])
print(lista[::-1])


carros = ['gol', 'celta', 'palio']

for carro in carros:
    print(carro)


for indice, carro in enumerate(carros):
    print(f'`{indice}: {carro}')


numeros = [1, 30, 21, 2, 9, 65, 34]
pares = []

for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)

print(pares)        


#list = [return for iteração in numeros condição]
pares = [numero for numero   in numeros if numero % 2 == 0]
print(pares)


quadrado = []
for numero in numeros:
    quadrado.append(numero ** 2)

print(quadrado)

quadrado = [numero ** 2 for numero in numeros]
print(quadrado)