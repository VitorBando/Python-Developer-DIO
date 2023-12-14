conjunto_a = {1, 2}
conjunto_b = {3, 4}

print(conjunto_a.union(conjunto_b))

conjunto_a = {1, 2, 3}
conjunto_b = {2, 3, 4}

print(conjunto_a.intersection(conjunto_b))

print(conjunto_a.difference(conjunto_b))
print(conjunto_b.difference(conjunto_a))
print(conjunto_a.symmetric_difference(conjunto_b))

conjunto_a = {1, 2, 3}
conjunto_b = {4, 1, 2, 5, 6, 3}

print(conjunto_a.issubset(conjunto_b))
print(conjunto_b.issubset(conjunto_a))
print(conjunto_a.issuperset(conjunto_b))
print(conjunto_b.issuperset(conjunto_a))

conjunto_a = {1, 2, 3, 4, 5}
conjunto_b = {6, 7, 8, 9}
conjunto_c = {1, 0}

print(conjunto_a.isdisjoint(conjunto_b))
print(conjunto_a.isdisjoint(conjunto_c))

sorteio = {1, 23}

sorteio.add(25)
sorteio.add(42)
sorteio.add(25)
print(sorteio)

sorteio.clear()
print(sorteio)

sorteio = {1, 23}

sorteio_2 = sorteio.copy()

sorteio_2.add(25)
sorteio_2.add(42)

print(sorteio)
print(sorteio_2)

numeros = {1, 2, 3, 1, 2, 4, 5, 5, 6, 7, 8, 9, 0}

print(numeros)
print(numeros.discard(1))
print(numeros.discard(45))
print(numeros)

print(numeros.pop())
print(numeros.pop())
print(numeros.pop())

numeros = {1, 2, 3, 1, 2, 4, 5, 5, 6, 7, 8, 9, 0}

print(numeros)
print(numeros.remove(1))
print(numeros.remove(9))
print(numeros)

print(len(numeros))

print(1 in numeros)
print(4 in numeros)

