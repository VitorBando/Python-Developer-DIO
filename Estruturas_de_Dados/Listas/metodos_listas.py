lista = []

lista.append(1)
lista.append('Python')
lista.append([40, 30, 20])

print(lista)


lista.clear()

print(lista)

lista = []

lista.append(1)
lista.append('Python')
lista.append([40, 30, 20])

lista_2 = lista.copy()
print(lista)

print(id(lista), id(lista_2))

lista_2[0] = 2

print(lista)
print(lista_2)

cores = ['Vermelho', 'Azul', 'Verde', 'Azul']
print(cores.count('Vermelho'))
print(cores.count('Azul'))
print(cores.count('Verde'))

linguagens = ['python', 'c', 'js', 'c']
print(linguagens)

linguagens.extend(['java', 'csharp'])
print(linguagens)

print(linguagens.index('java'))
print(linguagens.index('python'))

print(linguagens.pop())
print(linguagens)
print(linguagens.pop())
print(linguagens)
print(linguagens.pop())
print(linguagens)
print(linguagens.pop(0))
print(linguagens)

print(linguagens.remove('c'))
print(linguagens)

linguagens = ['python', 'c', 'js', 'c']
print(linguagens)

linguagens.extend(['java', 'csharp'])
print(linguagens)

linguagens.reverse()
print(linguagens)


linguagens = ['python', 'c', 'js', 'c']
print(linguagens)

linguagens.extend(['java', 'csharp'])
print(linguagens)

linguagens.sort()
print(linguagens)
linguagens.sort(reverse=True)
print(linguagens)
linguagens.sort(key=lambda x: len(x))
print(linguagens)
linguagens.sort(key=lambda x: len(x), reverse=True)
print(linguagens)


print(len(linguagens))

print(sorted(linguagens, key=lambda x: len(x)))
print(sorted(linguagens, key=lambda x: len(x), reverse=True))


